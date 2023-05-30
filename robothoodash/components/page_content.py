import dash_bootstrap_components as dbc
from dash import callback, dcc
from dash.dependencies import Input, Output
from plotly.graph_objs import Figure

from robothoodash.hoodapi.hoodapi import HoodApi
from robothoodash.visualization.plot_functions import (
    lineplot_base_currency_balance,
    plot_open_orders_table,
)

# pylint:disable=unused-variable
page_content = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(
                id="lineplot-base-currency-balance", figure={}, style={"padding-top": "5rem"}
            ),
        ),
        dbc.Col(
            plot_open_orders_table(data=HoodApi().get_open_orders()),
            style={"padding-top": "9rem"},
        ),
    ]
)


@callback(  # type:ignore
    Output("lineplot-base-currency-balance", "figure"),
    Input("radios-base-currency-selector", "value"),
)
def lineplot_base_currency_balance_callback(base_currency: str) -> Figure:
    """Get data and plot the line plot of the base currency balance

    Parameters
    ----------
    base_currency: str
        The base currency, either BTC or USDT

    Returns
    -------
    Figure
        The balance of base currency on a time line plot
    """
    client = HoodApi()
    data = client.get_balance_data(base_currency=base_currency)
    return lineplot_base_currency_balance(data=data, base_currency=base_currency)
