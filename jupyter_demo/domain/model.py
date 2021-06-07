from abc import abstractmethod
from typing import Dict, List, Optional

from pandas import DataFrame


class AbstractStructure:
    def __init__(self, dataframe: DataFrame, schema: Optional[Dict[str, any]]):
        # TODO: add some optional type checking of the dataframe content
        self.dataframe = dataframe
        self.schema = schema
        self._validate()

    @abstractmethod
    def display(self, *args):
        return NotImplemented

    @property
    def _dataframe_columns(self) -> List[str]:
        return sorted(self.dataframe.columns)

    @property
    def _schema_fields(self) -> List[str]:
        return sorted(self.schema.keys())

    def _validate(self) -> None:
        if self._dataframe_columns != self._schema_fields:
            raise ValueError(
                f"dataframe columns names do not match.\n"
                f"Want: {self._schema_fields},\n"
                f"Got: {self._dataframe_columns}"
            )
