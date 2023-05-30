import dash_bootstrap_components as dbc
from dash import html

ROBOTHOOD_LOGO = (
    "https://raw.githubusercontent.com/etnberz/dummy_robothood/master/static/img/robothood.png"
)

ROBOTHOOD_LINK = (
    "https://medium.com/@maxime.caitucoli/a-crypto-trading-bot-for-the-greater-good-1e04cb7bbe54"
)

# pylint:disable=unused-variable

navbar = dbc.Navbar(
    dbc.Container(
        [
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(
                        html.A(
                            html.Img(src=ROBOTHOOD_LOGO, height="80px"),
                            href=ROBOTHOOD_LINK,
                        ),
                        align="center",
                    ),
                    dbc.Col(
                        dbc.NavbarBrand(
                            "RobotHood Performances Monitoring",
                            style={
                                "font-size": "2.5em",
                                "font-weight": "700",
                                "font-family": "Inter, sans-serif",
                            },
                        ),
                        align="center",
                    ),
                    dbc.Col(
                        dbc.Nav(
                            html.Div(
                                [
                                    dbc.RadioItems(
                                        id="radios-base-currency-selector",
                                        className="btn-group",
                                        inputClassName="btn-check",
                                        labelClassName="btn btn-outline-primary",
                                        labelCheckedClassName="active",
                                        options=[
                                            {"label": "BTC", "value": "btc"},
                                            {"label": "USDT", "value": "usdt"},
                                        ],
                                        value="btc",
                                    ),
                                ],
                                className="radio-group",
                            )
                        ),
                        align="right",
                    ),
                ],
                align="center",
            ),
        ],
        fluid=True,
    ),
    color="#161613",
    dark=True,
    fixed="top",
    expand=True,
)
