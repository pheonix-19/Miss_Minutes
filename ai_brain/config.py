"""Environment-driven configuration for the AI brain."""

import os

from dotenv import load_dotenv

# Load variables from a local .env file if present.
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is required. Set it in your environment or .env file.")