from IPython.core.display import clear_output
from ipywidgets import interact_manual
from numpy import ndarray
from pandas import DataFrame

from content.controls.control import TVRadio


def display(tv_radio: TVRadio, data_frame: DataFrame):
    @interact_manual(
        state_name=tv_radio.state_names,
        licence_status=tv_radio.licence_status,
        service=tv_radio.service,
    )
    def _display(state_name: ndarray, licence_status: ndarray, service: ndarray):

        clear_output(wait=True)

        return data_frame[
            (data_frame["state_name"] == state_name)
            & (data_frame["status"] == licence_status)
            & (data_frame["service"] == service)
        ]
