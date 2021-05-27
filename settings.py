from decouple import config
from pathlib import Path

DATA_DIR = config('DATA_DIR', cast=Path)
RUN_QUERIES = config('RUN_QUERIES', cast=bool)