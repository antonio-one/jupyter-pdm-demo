from contextlib import suppress
from os import unlink
from pathlib import Path
from typing import Union

import pandas as pd
from google.cloud import bigquery
from google.cloud.bigquery.table import RowIterator, _EmptyRowIterator


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


class BigQueryRepository:
    def __init__(self, client: bigquery.Client):
        self.client = client

    def get_rows(self, sql_command: str) -> Union[RowIterator, _EmptyRowIterator]:
        query_job = self.client.query(sql_command)
        return query_job.result()

    def get_df(self, sql_command: str) -> pd.DataFrame:
        query_job = self.client.query(sql_command)
        result = query_job.result()
        return result.to_dataframe()


class PostgreRepository:
    def __init__(self):
        pass

    # noinspection PyMethodMayBeStatic
    def get_rows(self):
        return NotImplemented

    # noinspection PyMethodMayBeStatic
    def get_df(self):
        return NotImplemented
