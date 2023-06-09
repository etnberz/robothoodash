import dash_bootstrap_components as dbc
from dash import callback, dcc
from dash.dash_table import DataTable
from dash.dependencies import Input, Output
from plotly.graph_objs import Figure

from robothoodash.hoodapi.hoodapi import HoodApi
from robothoodash.visualization.plot_functions import (
    barplot_profit,
    lineplot_base_currency_balance,
    plot_open_orders_table,
)

# pylint:disable=unused-variable
page_content = [
    dbc.Row(
        [
            dbc.Col(
                dcc.Graph(
                    id="lineplot-base-currency-balance", figure={}, style={"padding-top": "5rem"}
                ),
            ),
            dbc.Col(id="col-orders", children=None, style={"padding-top": "8rem"}),
        ],
    ),
    dbc.Row(
        [
            dbc.Col(
                dbc.Row(
                    [
                        dcc.Graph(id="barplot-profit", figure={}),
                        dbc.RadioItems(
                            id="time-window-barplot-selector",
                            className="btn-group",
                            inputClassName="btn-check",
                            labelClassName="btn btn-outline-primary",
                            labelCheckedClassName="active",
                            options=[
                                {"label": "Month", "value": "month"},
                                {"label": "Week", "value": "week"},
                                {"label": "Day", "value": "day"},
                            ],
                            value="day",
                            inline=True,
                        ),
                    ]
                ),
            )
        ]
    ),
]


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
    client = HoodApi(base_currency=base_currency)
    data = client.get_balance_data()
    return lineplot_base_currency_balance(data=data, base_currency=base_currency)


@callback(  # type:ignore
    Output("col-orders", "children"),
    Input("radios-base-currency-selector", "value"),
)
def plot_open_orders_table_callback(base_currency: str) -> DataTable:
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
    client = HoodApi(base_currency=base_currency)
    data = client.get_open_orders()
    return plot_open_orders_table(data=data)


@callback(  # type:ignore
    Output("barplot-profit", "figure"),
    [
        Input("radios-base-currency-selector", "value"),
        Input("time-window-barplot-selector", "value"),
    ],
)
def barplot_profit_callback(base_currency: str, granularity: str) -> Figure:
    """Get data and plot the line plot of the base currency balance

    Parameters
    ----------
    base_currency: str
        The base currency, either BTC or USDT
    granularity: str
        The time granularity

    Returns
    -------
    Figure
        The balance of base currency on a time line plot
    """
    client = HoodApi(base_currency=base_currency)
    data = client.get_profit(granularity=granularity)
    return barplot_profit(data=data, base_currency=base_currency)
