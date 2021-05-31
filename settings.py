from pathlib import Path

from decouple import config

PROJECT_ID = config("PROJECT_ID", cast=str)
DATA_DIR = config("DATA_DIR", cast=Path)
RUN_QUERIES = False
