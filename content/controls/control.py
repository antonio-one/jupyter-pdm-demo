from ipywidgets import IntSlider
from numpy import ndarray
from pandas import DataFrame


class InteractiveAbstract:
    pass


class TVRadio(InteractiveAbstract):
    def __init__(self, data_frame: DataFrame):
        self.data_frame = data_frame

    @property
    def state_names(self) -> ndarray:
        _state_names = self.data_frame["state_name"].unique()
        _state_names.sort()
        return _state_names

    @property
    def licence_status(self) -> ndarray:
        _licence_status = self.data_frame["status"].unique()
        _licence_status.sort()
        return _licence_status

    @property
    def service(self) -> ndarray:
        _service = self.data_frame["service"].unique()
        _service.sort()
        return _service

    @property
    def min_stations(self) -> IntSlider:
        return IntSlider(
            min=1, max=self.data_frame["number_of_stations"].max(), step=1, value=1
        )

    @property
    def max_stations(self) -> IntSlider:
        return IntSlider(
            min=1,
            max=self.data_frame["number_of_stations"].max(),
            step=1,
            value=int(self.data_frame["number_of_stations"].max() / 2),
        )

    @property
    def bins(self) -> IntSlider:
        return IntSlider(min=1, max=100, step=1, value=20)
