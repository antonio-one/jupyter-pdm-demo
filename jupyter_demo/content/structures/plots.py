import warnings

import matplotlib.pyplot as plt
import mplcursors
from geopandas import GeoDataFrame
from geopandas import datasets as geo_datasets
from geopandas import read_file
from IPython.core.display import clear_output
from ipywidgets import interact_manual
from ipywidgets.widgets.widget_int import IntSlider
from numpy import ndarray
from pandas import DataFrame
from shapely.geometry.point import Point

from jupyter_demo.domain.model import AbstractStructure


class Distribution(AbstractStructure):
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
            service=self.service,
            min_stations=self.min_stations,
            max_stations=self.max_stations,
            bins=self.bins,
        )
        def _display(
            service: ndarray,
            min_stations: IntSlider,
            max_stations: IntSlider,
            bins: IntSlider,
        ):
            clear_output(wait=True)

            plot_df = self.dataframe[
                (self.dataframe["service"] == service)
                & (self.dataframe["number_of_stations"] > min_stations)
                & (self.dataframe["number_of_stations"] <= max_stations)
            ]

            fig, ax = plt.subplots()

            ax.set_title("Distribution of Number of Stations")
            ax.set_xlabel("Number of Stations")
            ax.set_ylabel("Number of Cities")

            ax.hist(
                plot_df["number_of_stations"],
                bins=bins,
                histtype="bar",
                label="Stations",
            )

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

    @property
    def bins(self) -> IntSlider:
        return IntSlider(min=1, max=100, step=1, value=20)


class USMap(AbstractStructure):
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
        @interact_manual(service=self.service, status=self.licence_status)
        def _display(
            service: ndarray,
            status: ndarray,
        ):
            plt.close()

            _geo_tv_radio_station_df = self.dataframe[
                (self.dataframe["service"] == service)
                & (self.dataframe["status"] == status)
            ]

            _geometry = [
                Point(xy)
                for xy in zip(
                    _geo_tv_radio_station_df["lng"], _geo_tv_radio_station_df["lat"]
                )
            ]

            _geometry_df = GeoDataFrame(_geo_tv_radio_station_df, geometry=_geometry)

            fig, ax = plt.subplots()
            ax.set_title(f"US {status.title()} {service}")

            world = read_file(geo_datasets.get_path("naturalearth_lowres"))
            north_america = world.query('continent == "North America"')
            north_america.plot(ax=ax, alpha=0.2, color="#00296b", edgecolor="#faf6f6")

            for i in range(_geometry_df["number_of_stations"].max()):
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", UserWarning)
                    _geometry_df[_geometry_df["number_of_stations"] == i].plot(
                        ax=ax,
                        alpha=0.5,
                        markersize=i * 10,
                        label=_geometry_df["number_of_stations"],
                    )

                labels = _geometry_df["city"].unique()
                mplcursors.cursor(ax).connect(
                    "add", lambda sel: sel.annotation.set_text(labels[sel.target.index])
                )

            plt.show()

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
