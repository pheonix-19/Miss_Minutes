import sys
from pathlib import Path

from .ai.intent_parser import process_input

# Load system prompt from ai/prompt.txt relative to this file's location
prompt_path = Path(__file__).parent / "ai" / "prompt.txt"
with open(prompt_path, "r") as f:
    SYSTEM_PROMPT = f.read()

print("🤖 Emo Bot AI Ready (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    result = process_input(SYSTEM_PROMPT, user_input)

    print("\n--- AI OUTPUT ---")
    print("Type   :", result["type"])
    print("Command:", result["command"])
    print("Emotion:", result["emotion"])
    print("Reply  :", result["reply"])
    print("-----------------\n")
