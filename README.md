## jupyter-demo

This demo relies on public google bigquery data.

```
export PROJECT_ID=your_gcp_project_id
```

Authenticate the app with the below before you start playing with the notebook.
```
gcloud auth application-default login
```

Change the `RUN_QUERIES = True` in `settings.py` if you want to run the SQL query. This is used to prevent unnecessary executions once the query result has been stored locally. _Note this approach is not recommended for large datasets_.

### Reading Materials
- [Interacting with bigquery](https://github.com/googleapis/python-bigquery/blob/35627d145a41d57768f19d4392ef235928e00f72/samples/client_query_destination_table.py)
- [pandas.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)
- [matplotlib.pyplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html?highlight=pyplot%20plot#module-matplotlib.pyplot)
- [Using Interact](https://ipywidgets.readthedocs.io/en/stable/examples/Using%20Interact.html#Basic-interact)
- [geopandas.org](https://geopandas.org/docs/user_guide/mapping.html)
- [Plot any data with a latitude and longitude on a map](https://towardsdatascience.com/geopandas-101-plot-any-data-with-a-latitude-and-longitude-on-a-map-98e01944b972)
- [Cosmic Python](https://www.cosmicpython.com/)

### Credits and Data
* `content/data/uscities.csv` appears courtesy of [simplemaps.com](https://simplemaps.com/data/us-cities.)
