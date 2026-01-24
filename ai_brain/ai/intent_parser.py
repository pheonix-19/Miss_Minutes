import json

from .openai_client import ask_ai

def process_input(system_prompt, user_text):
    raw_response = ask_ai(system_prompt, user_text)

    try:
        data = json.loads(raw_response)
        return data
    except json.JSONDecodeError:
        return {
            "type": "chat",
            "command": "NONE",
            "emotion": "NEUTRAL",
            "reply": raw_response
        }
