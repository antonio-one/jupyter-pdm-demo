from pathlib import Path
import pandas as pd
from os import unlink
from contextlib import suppress


class DataFrameRepository:
    def __init__(self, repository_path: Path):
        self.repository_path = repository_path

    def add(self, data_frame: pd.DataFrame, filename: str) -> Path:
        return data_frame.to_feather(self.filepath(filename))

    def get(self, filename: str) -> pd.DataFrame:
        return pd.read_feather(self.filepath(filename))

    def remove(self, filename: str) -> bool:
        with suppress(FileNotFoundError):
            unlink(self.filepath(filename))

    def filepath(self, filename: str) -> Path:
        return self.repository_path / filename
