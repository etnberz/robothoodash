import os

import duckdb
import plotly.express as px
from plotly.graph_objs import Figure


class PlotManager:
    """The plot manager for our dashboard"""

    def __init__(self) -> None:
        duckdb.load_extension(extension="sqlite_scanner")
        self.con = duckdb.connect(os.environ["ROBOTHOOD_DB_PATH"])

    def plot_line_balance(self, base_currency: str) -> Figure:
        """Plot the balance of base currency on a time line

        Parameters
        ----------
        base_currency: str
            The base currency, either BTC or USDT

        Returns
        -------
        Figure
            The balance of base currency on a time line plot

        """
        return px.line(
            self.con.sql(f"""SELECT {base_currency}_balance FROM tracker""").pl()
        ).update_layout(
            title="YOOO",
            xaxis_title="Time",
            yaxis_title=f"{base_currency.upper()} Balance",
            showlegend=False,
            hovermode="x",
        )
