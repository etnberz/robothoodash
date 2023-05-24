import os

import dash_bootstrap_components as dbc
import flask
from dash import Dash, dcc, html

from robothoodash.components.navbar import navbar
from robothoodash.visualization.plot_manager import PlotManager

server = flask.Flask(__name__)
app = Dash(
    __name__,
    server=server,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    title="RobotHooDash",
)
os.environ["ROBOTHOOD_DB_PATH"] = "/home/maxime/code/robothood/database/robothood.db"

plot_manager = PlotManager()

CONTENT_STYLE = {
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

content = html.Div(
    [
        html.H2(
            "Base Currencies Balances",
            style={"padding-top": "5rem"},
        ),
        dcc.Graph(
            id="line-balance-usdt", figure=plot_manager.plot_line_balance(base_currency="usdt")
        ),
    ]
)

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        navbar,
        dbc.Container(
            [
                content,
            ],
            fluid=True,
        ),
    ],
    style=CONTENT_STYLE,
)

if __name__ == "__main__":
    app.run_server(debug=True)
