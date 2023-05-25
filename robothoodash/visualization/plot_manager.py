import pandas as pd
import plotly.express as px
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
        y=f"{base_currency.lower()}_balance",
        title=f"{base_currency.upper()} Balance Evolution",
    ).update_layout(
        xaxis_title="",
        yaxis_title=f"{base_currency.upper()} Balance",
        showlegend=False,
        hovermode="x",
    )
