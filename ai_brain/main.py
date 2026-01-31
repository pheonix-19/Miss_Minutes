from pathlib import Path

from .ai.intent_parser import process_input
from .voice.mic_input import listen
from .voice.tts import speak
from .robot_link.serial_comm import PicoDisplay
from .robot_link.command_map import COMMAND_MAP

# Initialize Pico display connection
try:
    pico = PicoDisplay(port="COM5")  # Change to your port if different
except Exception as e:
    print(f"[WARN] Pico not connected: {e}")
    pico = None

prompt_path = Path(__file__).parent / "ai" / "prompt.txt"
with open(prompt_path, "r") as f:
    SYSTEM_PROMPT = f.read()

speak("Hello! I am Emo Bot. How can I help you?")

while True:
    user_text = listen()

    if not user_text:
        speak("Sorry, I didn't catch that.")
        continue

    if user_text.lower() in ["exit", "quit", "stop"]:
        speak("Goodbye! See you soon.")
        break

    result = process_input(SYSTEM_PROMPT, user_text)
    print("[DEBUG] Result:", result)

    # Print command & emotion
    print("Type   :", result.get("type"))
    print("Command:", result.get("command"))
    print("Emotion:", result.get("emotion"))
    
    # Send command and emotion to Pico display (always show emotion)
    command = result.get("command", "NONE")
    emotion = result.get("emotion", "NEUTRAL")
    if pico:
        if command != "NONE":
            pico_cmd = COMMAND_MAP.get(command, command)
            pico.show(f"{pico_cmd} ({emotion})")
            print(f"[PICO] Sent: {pico_cmd} ({emotion})")
        else:
            # For chat, just show emotion
            pico.show(f"CHAT ({emotion})")
            print(f"[PICO] Sent: CHAT ({emotion})")

    # Speak AI reply (after screen update)
    if result.get("reply"):
        speak(result["reply"])
    else:
        print("[DEBUG] No reply in result")
