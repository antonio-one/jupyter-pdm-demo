from IPython.core.display import clear_output
from ipywidgets import interact_manual
import matplotlib.pyplot as plt
from content.controls.control import TVRadio
from pandas import DataFrame
from numpy import ndarray
from ipywidgets.widgets.widget_int import IntSlider


def display(tv_radio: TVRadio, data_frame: DataFrame):
    @interact_manual(
        service=tv_radio.service,
        min_stations=tv_radio.min_stations,
        max_stations=tv_radio.max_stations,
        bins=tv_radio.bins,
    )
    def _display(
            service: ndarray,
            min_stations: IntSlider,
            max_stations: IntSlider,
            bins: IntSlider
    ):

        clear_output(wait=True)

        plot_df = data_frame[
            (data_frame['service'] == service)
            & (data_frame['number_of_stations'] > min_stations)
            & (data_frame['number_of_stations'] <= max_stations)
        ]

        fig, ax = plt.subplots()

        ax.set_title('Distribution of Number of Stations')
        ax.set_xlabel('Number of Stations')
        ax.set_ylabel('Number of Cities')

        ax.hist(
            plot_df['number_of_stations'],
            bins=bins,
            histtype='bar',
            label='Stations'
        )
