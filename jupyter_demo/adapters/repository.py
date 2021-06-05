from abc import abstractmethod
from contextlib import suppress
from os import unlink
from pathlib import Path
from typing import Union

from google.cloud import bigquery
from google.cloud.bigquery.table import RowIterator, _EmptyRowIterator
from pandas import DataFrame, read_feather


class AbstractRepository:
    @abstractmethod
    def get(self, *args):
        raise NotImplementedError


class DataFrameRepository(AbstractRepository):
    def __init__(self, path: Path):
        self.path = path

    def add(self, data_frame: DataFrame, filename: str) -> Path:
        DataFrame.to_feather(
            data_frame, path=self._filepath(filename), compression="zstd"
        )
        return self._filepath(filename)

    def get(self, filename: str) -> DataFrame:
        return read_feather(self._filepath(filename))

    def remove(self, filename: str) -> None:
        with suppress(FileNotFoundError):
            unlink(self._filepath(filename))

    def _filepath(self, filename: str) -> Union[Path, str]:
        return self.path / filename


class BigQueryRepository(AbstractRepository):
    def __init__(self, client: bigquery.Client):
        self.client = client

    def get(self, sql_command: str) -> DataFrame:
        query_job = self.client.query(sql_command)
        result = query_job.result()
        return result.to_dataframe(progress_bar_type="tqdm_notebook")

    def get_rows(self, sql_command: str) -> Union[RowIterator, _EmptyRowIterator]:
        query_job = self.client.query(sql_command)
        return query_job.result()
