"""Mic capture without PyAudio using sounddevice + SpeechRecognition."""

import speech_recognition as sr
import sounddevice as sd
import numpy as np

recognizer = sr.Recognizer()


def listen(duration: float = 4.0, sample_rate: int = 16_000) -> str | None:
    """Capture audio for a few seconds and transcribe via Google Speech.

    Avoids PyAudio by recording with sounddevice and feeding raw bytes to
    SpeechRecognition. Duration and sample_rate are adjustable.
    """

    print("🎤 Listening...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="int16")
    sd.wait()

    # Convert to bytes for SpeechRecognition
    audio_bytes = audio.tobytes()
    audio_data = sr.AudioData(audio_bytes, sample_rate, 2)  # 2 bytes per sample (int16)

    try:
        text = recognizer.recognize_google(audio_data)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print("Speech error:", e)
        return None
