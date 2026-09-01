"""Central config. Reads from environment / .env so secrets stay out of code."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = Path(os.getenv("DATA_DIR", PROJECT_ROOT / "data"))
DB_PATH = Path(os.getenv("DB_PATH", DATA_DIR / "app.db"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

DATA_DIR.mkdir(parents=True, exist_ok=True)
