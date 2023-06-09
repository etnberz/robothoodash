import dash_bootstrap_components as dbc
import flask
from dash import Dash, dcc, html

from robothoodash.components.navbar import navbar
from robothoodash.components.page_content import page_content

server = flask.Flask(__name__)
app = Dash(
    __name__,
    server=server,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    title="RobotHooDash",
)

CONTENT_STYLE = {
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        navbar,
        dbc.Container(
            page_content,
            fluid=True,
        ),
    ],
    style=CONTENT_STYLE,
)

if __name__ == "__main__":
    app.run_server(debug=True)
