import dash_bootstrap_components as dbc
import flask
from dash import Dash, html

server = flask.Flask(__name__)
app = Dash(
    __name__,
    server=server,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    title="RobotHooDash",
)

app.layout = html.Div(
    [
        html.H2(
            "Welcome to RobotHooDash: quite naked now, see future versions for more content",
            style={"padding-top": "5rem"},
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
