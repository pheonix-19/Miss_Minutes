# Miss Minutes

PC-side AI brain and Pico firmware scaffold for the Miss Minutes robot.

## Quick start
- Create a virtual env (example): `python -m venv .venv` then activate it.
- Install deps: `pip install -r requirements.txt`.
- Copy `.env.example` to `.env` and set `OPENAI_API_KEY`; optional `MODEL_NAME` (default: gpt-4.1-mini).
- Run the AI brain REPL from repo root: `python -m ai_brain.main`.
