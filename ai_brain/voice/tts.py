"""Text-to-speech using gTTS (Google Text-to-Speech)."""

import os
import tempfile
import winsound

from gtts import gTTS
from pydub import AudioSegment


def speak(text: str) -> None:
    """Speak the given text aloud using gTTS."""
    if not text or not text.strip():
        return

    try:
        print("🤖:", text)
        
        # Generate speech using Google TTS (with timeout)
        tts = gTTS(text, lang="en", slow=False)
        
        # Save to temp MP3
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_mp3:
            tmp_mp3_path = tmp_mp3.name
        
        try:
            tts.save(tmp_mp3_path)
        except (KeyboardInterrupt, TimeoutError, OSError) as e:
            print(f"[TTS] Network issue, skipping audio: {type(e).__name__}")
            return
        
        # Convert MP3 to WAV
        try:
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_wav:
                tmp_wav_path = tmp_wav.name
            
            sound = AudioSegment.from_mp3(tmp_mp3_path)
            sound.export(tmp_wav_path, format="wav")
            
            # Play WAV with winsound
            winsound.PlaySound(tmp_wav_path, winsound.SND_FILENAME)
        except Exception as e:
            print(f"[TTS] Playback error: {e}")
        finally:
            # Clean up temp files
            try:
                os.remove(tmp_mp3_path)
            except:
                pass
            try:
                os.remove(tmp_wav_path)
            except:
                pass
            
    except Exception as e:
        print(f"[TTS Error] {type(e).__name__}: {e}")
