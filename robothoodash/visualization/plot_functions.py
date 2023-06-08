import numpy as np
import pandas as pd
import plotly.express as px
from dash import dash_table
from dash.dash_table import DataTable
from plotly.graph_objs import Figure

# pylint:disable=unused-variable


def lineplot_base_currency_balance(data: pd.DataFrame, base_currency: str) -> Figure:
    """Plot the balance of base currency on a time line

    Parameters
    ----------
    data: pd.DataFrame
        The time series data needed to plot the currency balance
    base_currency: str
        The base currency, either BTC or USDT

    Returns
    -------
    Figure
        The balance of base currency on a time line plot

    """
    return px.line(
        data,
        x="timestamp",
        y=f"{base_currency}_balance",
        title=f"{base_currency.upper()} Balance Evolution",
    ).update_layout(
        xaxis_title="",
        yaxis_title=f"{base_currency.upper()} Balance",
        showlegend=False,
        hovermode="x",
    )


def plot_open_orders_table(data: pd.DataFrame) -> DataTable:
    """Plot the data table of open orders

    Parameters
    ----------
    data: pd.DataFrame
        Open order dataframe

    Returns
    -------
    DataTable
        The data table to display
    """
    return dash_table.DataTable(
        data.to_dict("records"),
        columns=[{"name": i.upper(), "id": i} for i in data.columns],
        id="tbl",
        fixed_rows={"headers": True},
        style_table={"height": 300},
        style_header={
            "backgroundColor": "rgb(30, 30, 30)",
            "textAlign": "center",
            "color": "white",
        },
        style_data={
            "backgroundColor": "rgb(50, 50, 50)",
            "textAlign": "center",
            "color": "white",
        },
    )


def barplot_profit(data: pd.DataFrame, base_currency: str) -> Figure:
    """Plot the profit bar-plot

    Parameters
    ----------
    data: pd.DataFrame
        The time series data needed to plot the currency balance
    base_currency: str
        The base currency, either BTC or USDT

    Returns
    -------
    Figure
        The balance of base currency on a time line plot
    """
    profit = f"{base_currency}_profit"
    return px.bar(
        data_frame=data,
        x="period",
        y=profit,
        title=f"{base_currency.upper()} Profit Loss Graph",
        color=np.where(data[profit] >= 0, "green", "red"),
        color_discrete_map={"red": "#eb2a2a", "green": "#4deb2a"},
        hover_data={
            "period": True,
            profit: ":.6f",
        },
    ).update_layout(
        xaxis_title="",
        yaxis_title=f"{base_currency.upper()} Profit",
        showlegend=False,
        hovermode="x",
    )
