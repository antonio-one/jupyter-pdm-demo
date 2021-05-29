from pathlib import Path

from decouple import config

DATA_DIR = config("DATA_DIR", cast=Path)
RUN_QUERIES = config("RUN_QUERIES", cast=bool)
