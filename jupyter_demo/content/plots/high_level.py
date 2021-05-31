from IPython.core.display import clear_output
from ipywidgets import interact_manual
from ipywidgets.widgets.widget_int import IntSlider
from pandas import DataFrame

from jupyter_demo.content.controls.control import TVRadio


def display(tv_radio: TVRadio, data_frame: DataFrame):
    @interact_manual(
        min_stations=tv_radio.min_stations, max_stations=tv_radio.max_stations
    )
    def _display(min_stations: IntSlider, max_stations: IntSlider):

        clear_output(wait=True)

        return data_frame[
            (data_frame["number_of_stations"] > min_stations)
            & (data_frame["number_of_stations"] <= max_stations)
        ].sort_values(by="number_of_stations", ascending=False)
