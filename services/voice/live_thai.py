import os

from google import genai
from google.genai import types

from core.language.thai_policy import THAI_SYSTEM_INSTRUCTION
from services.voice.audio_config import (
    LIVE_MODEL,
    DEFAULT_VOICE,
)


def create_client() -> genai.Client:
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "ไม่พบ GEMINI_API_KEY ใน environment"
        )

    return genai.Client(api_key=api_key)


def create_live_config() -> types.LiveConnectConfig:
    return types.LiveConnectConfig(
        response_modalities=["AUDIO"],

        system_instruction=THAI_SYSTEM_INSTRUCTION,

        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name=DEFAULT_VOICE
                )
            )
        ),

        input_audio_transcription=types.AudioTranscriptionConfig(),

        output_audio_transcription=types.AudioTranscriptionConfig(),
    )


def health() -> dict:
    return {
        "status": "READY",
        "language": "th-TH",
        "language_name": "ภาษาไทย",
        "voice": DEFAULT_VOICE,
        "model": LIVE_MODEL,
        "input_transcription": True,
        "output_transcription": True,
        "governance_bypass": False,
        "transaction_execution": False,
    }
