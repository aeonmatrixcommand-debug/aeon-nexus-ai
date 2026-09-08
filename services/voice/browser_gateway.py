import asyncio
import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from google.genai import types

from services.voice.live_thai import (
    create_client,
    create_live_config,
)
from services.voice.audio_config import LIVE_MODEL


router = APIRouter()


@router.websocket("/ws/voice/th")
async def thai_voice_socket(websocket: WebSocket):
    await websocket.accept()

    client = create_client()
    config = create_live_config()

    async with client.aio.live.connect(
        model=LIVE_MODEL,
        config=config,
    ) as session:

        await websocket.send_json(
            {
                "type": "status",
                "status": "CONNECTED",
                "language": "th-TH",
                "model": LIVE_MODEL,
                "governance_bypass": False,
                "transaction_execution": False,
            }
        )

        async def browser_to_gemini():
            try:
                while True:
                    message = await websocket.receive()

                    if message["type"] == "websocket.disconnect":
                        return

                    audio = message.get("bytes")

                    if audio:
                        await session.send_realtime_input(
                            audio=types.Blob(
                                data=audio,
                                mime_type="audio/pcm;rate=16000",
                            )
                        )
                        continue

                    text_message = message.get("text")

                    if not text_message:
                        continue

                    try:
                        payload = json.loads(text_message)
                    except json.JSONDecodeError:
                        continue

                    message_type = payload.get("type")

                    if message_type == "audio_end":
                        await session.send_realtime_input(
                            audio_stream_end=True
                        )

            except WebSocketDisconnect:
                return

        async def gemini_to_browser():
            async for response in session.receive():
                content = response.server_content

                if not content:
                    continue

                input_transcription = getattr(
                    content,
                    "input_transcription",
                    None,
                )

                if (
                    input_transcription
                    and input_transcription.text
                ):
                    await websocket.send_json(
                        {
                            "type": "input_transcript",
                            "text": input_transcription.text,
                        }
                    )

                output_transcription = getattr(
                    content,
                    "output_transcription",
                    None,
                )

                if (
                    output_transcription
                    and output_transcription.text
                ):
                    await websocket.send_json(
                        {
                            "type": "output_transcript",
                            "text": output_transcription.text,
                        }
                    )

                if content.model_turn:
                    for part in content.model_turn.parts:
                        if (
                            part.inline_data
                            and part.inline_data.data
                        ):
                            await websocket.send_bytes(
                                part.inline_data.data
                            )

                if getattr(content, "interrupted", False):
                    await websocket.send_json(
                        {
                            "type": "interrupted",
                        }
                    )

                if content.turn_complete:
                    await websocket.send_json(
                        {
                            "type": "turn_complete",
                        }
                    )

        sender = asyncio.create_task(browser_to_gemini())
        receiver = asyncio.create_task(gemini_to_browser())

        done, pending = await asyncio.wait(
            {sender, receiver},
            return_when=asyncio.FIRST_COMPLETED,
        )

        for task in pending:
            task.cancel()

        await asyncio.gather(
            *pending,
            return_exceptions=True,
        )
