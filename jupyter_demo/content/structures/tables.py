from IPython.core.display import clear_output
from ipywidgets import interact_manual
from ipywidgets.widgets.widget_int import IntSlider
from numpy import ndarray
from pandas import DataFrame

from jupyter_demo.domain.model import AbstractStructure


class HighLevelTable(AbstractStructure):
    def __init__(self, dataframe: DataFrame):
        self.dataframe = dataframe
        self.schema = {
            "state_name": str,
            "number_of_stations": int,
        }
        super().__init__(dataframe, schema=self.schema)

    def display(self):
        @interact_manual(min_stations=self.min_stations, max_stations=self.max_stations)
        def _display(min_stations: IntSlider, max_stations: IntSlider):

            clear_output(wait=True)

            return self.dataframe[
                (self.dataframe["number_of_stations"] > min_stations)
                & (self.dataframe["number_of_stations"] <= max_stations)
            ].sort_values(by="number_of_stations", ascending=False)

    @property
    def min_stations(self) -> IntSlider:
        return IntSlider(
            min=1, max=self.dataframe["number_of_stations"].max(), step=1, value=1
        )

    @property
    def max_stations(self) -> IntSlider:
        return IntSlider(
            min=1,
            max=self.dataframe["number_of_stations"].max(),
            step=1,
            value=int(self.dataframe["number_of_stations"].max() / 2),
        )


class MoreDetailTable(AbstractStructure):
    def __init__(self, dataframe: DataFrame):
        self.dataframe = DataFrame
        self.schema = {
            "city": str,
            "state_name": str,
            "lat": float,
            "lng": float,
            "service": str,
            "status": str,
            "number_of_stations": int,
        }
        super().__init__(dataframe, schema=self.schema)

    def display(self):
        @interact_manual(
            state_name=self.state_names,
            licence_status=self.licence_status,
            service=self.service,
            min_stations=self.min_stations,
            max_stations=self.max_stations,
        )
        def _display(
            state_name: ndarray,
            licence_status: ndarray,
            service: ndarray,
            min_stations: IntSlider,
            max_stations: IntSlider,
        ):
            return self.dataframe[
                (self.dataframe["state_name"] == state_name)
                & (self.dataframe["status"] == licence_status)
                & (self.dataframe["service"] == service)
                & (self.dataframe["number_of_stations"] > min_stations)
                & (self.dataframe["number_of_stations"] <= max_stations)
            ]

    @property
    def state_names(self) -> ndarray:
        _state_names = self.dataframe["state_name"].unique()
        _state_names.sort()
        return _state_names

    @property
    def licence_status(self) -> ndarray:
        _licence_status = self.dataframe["status"].unique()
        _licence_status.sort()
        return _licence_status

    @property
    def service(self) -> ndarray:
        _service = self.dataframe["service"].unique()
        _service.sort()
        return _service

    @property
    def min_stations(self) -> IntSlider:
        return IntSlider(
            min=1, max=self.dataframe["number_of_stations"].max(), step=1, value=1
        )

    @property
    def max_stations(self) -> IntSlider:
        return IntSlider(
            min=1,
            max=self.dataframe["number_of_stations"].max(),
            step=1,
            value=int(self.dataframe["number_of_stations"].max() / 2),
        )
