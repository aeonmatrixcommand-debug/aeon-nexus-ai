import asyncio
import wave
from pathlib import Path

from services.voice.live_thai import (
    create_client,
    create_live_config,
)
from services.voice.audio_config import LIVE_MODEL


OUTPUT_FILE = Path("thai_live_test.wav")


async def main():
    client = create_client()
    config = create_live_config()

    audio_chunks = []
    transcript_parts = []

    print("กำลังเชื่อมต่อ Gemini Live...")
    print(f"Model: {LIVE_MODEL}")

    async with client.aio.live.connect(
        model=LIVE_MODEL,
        config=config,
    ) as session:

        print("Live Session: CONNECTED")

        await session.send_realtime_input(
            text=(
                "กรุณาตอบเป็นภาษาไทยสั้น ๆ ว่า "
                "ระบบเสียงภาษาไทยของ AEON MATRIX พร้อมใช้งาน"
            )
        )

        async for response in session.receive():
            server_content = response.server_content

            if not server_content:
                continue

            if server_content.output_transcription:
                text = server_content.output_transcription.text
                if text:
                    transcript_parts.append(text)
                    print("ข้อความตอบกลับ:", text)

            if server_content.model_turn:
                for part in server_content.model_turn.parts:
                    if part.inline_data and part.inline_data.data:
                        audio_chunks.append(part.inline_data.data)

            if server_content.turn_complete:
                break

    if not audio_chunks:
        raise RuntimeError(
            "เชื่อมต่อสำเร็จ แต่ไม่ได้รับข้อมูลเสียงจากโมเดล"
        )

    with wave.open(str(OUTPUT_FILE), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(b"".join(audio_chunks))

    print()
    print("LIVE VOICE TEST: PASSED")
    print("ภาษา: th-TH")
    print("ไฟล์เสียง:", OUTPUT_FILE)
    print("Governance bypass: FALSE")
    print("Transaction execution: FALSE")


if __name__ == "__main__":
    asyncio.run(main())
