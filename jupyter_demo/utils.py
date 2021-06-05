from types import ModuleType

from google.cloud import bigquery
from pandas import DataFrame

from jupyter_demo.adapters.repository import BigQueryRepository, DataFrameRepository
from jupyter_demo.options.interactive import set_interactive_opts
from jupyter_demo.options.pandas import set_pandas_opts
from jupyter_demo.options.plot import set_plot_opts
from settings import DATA_DIR, PROJECT_ID


def query_or_load(module: ModuleType, refresh=False) -> DataFrame:

    filename = f'{getattr(module, "__name__").split(".")[-1]}.feather'
    filepath = DATA_DIR / filename

    dfr = DataFrameRepository(path=DATA_DIR)

    if not filepath.is_file() or refresh:
        bqr = BigQueryRepository(client=bigquery.Client(project=PROJECT_ID))
        data_frame = bqr.get(sql_command=module.sql_command)
        dfr.add(data_frame=data_frame, filename=filename)
    else:
        data_frame = dfr.get(filename)

    return data_frame


def set_notebook_options():
    set_pandas_opts()
    set_plot_opts()
    set_interactive_opts()
