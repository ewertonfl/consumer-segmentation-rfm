import os
from pathlib import Path

# Define a raiz do projeto
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Define caminhos
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
SILVER_DATA_DIR = DATA_DIR / "silver"
GOLD_DATA_DIR = DATA_DIR / "gold"

# Garante que pastas existam
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
SILVER_DATA_DIR.mkdir(parents=True, exist_ok=True)
GOLD_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Procura o arquivo
POSSIBLE_FILES = list(RAW_DATA_DIR.glob("*.xlsx")) + list(RAW_DATA_DIR.glob("*.csv"))
RAW_DATA_FILE = POSSIBLE_FILES[0] if POSSIBLE_FILES else None