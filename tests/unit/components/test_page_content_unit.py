from contextvars import copy_context

import pandas as pd
import pytest
from dash._callback_context import context_value
from dash._utils import AttributeDict
from dash.dash_table import DataTable
from plotly.graph_objs import Figure

from robothoodash.components.page_content import (
    barplot_profit_callback,
    lineplot_base_currency_balance_callback,
    plot_open_orders_table_callback,
)
from robothoodash.hoodapi.hoodapi import ALLOWED_BASE_CURRENCY


@pytest.mark.parametrize("base_currency", ALLOWED_BASE_CURRENCY, ids=ALLOWED_BASE_CURRENCY)
def test_lineplot_base_currency_balance_callback(
    mock_duckdb_connection, base_currency
):  # pylint:disable=unused-argument
    def run_callback():
        context_value.set(
            AttributeDict(
                **{"triggered_inputs": [{"prop_id": "radios-base-currency-selector.value"}]}
            )
        )
        return lineplot_base_currency_balance_callback(base_currency=base_currency)

    ctx = copy_context()
    output = ctx.run(run_callback)
    assert isinstance(output, Figure)
    assert output.layout.yaxis["title"]["text"] == f"{base_currency.upper()} Balance"


@pytest.mark.parametrize("base_currency", ALLOWED_BASE_CURRENCY, ids=ALLOWED_BASE_CURRENCY)
def test_plot_open_orders_table_callback(
    mock_duckdb_connection, base_currency
):  # pylint:disable=unused-argument
    def run_callback():
        context_value.set(
            AttributeDict(
                **{"triggered_inputs": [{"prop_id": "radios-base-currency-selector.value"}]}
            )
        )
        return plot_open_orders_table_callback(base_currency=base_currency)

    ctx = copy_context()
    output = ctx.run(run_callback)
    assert isinstance(output, DataTable)
    assert all(pd.DataFrame(output.data)["base_currency"] == base_currency.upper())


@pytest.mark.parametrize(
    "base_currency, granularity",
    [
        ("btc", "day"),
        ("usdt", "day"),
        ("btc", "week"),
        ("usdt", "week"),
        ("btc", "month"),
        ("usdt", "month"),
    ],
)
def test_barplot_profit_callback(
    mock_duckdb_connection, base_currency, granularity
):  # pylint:disable=unused-argument
    def run_callback():
        context_value.set(
            AttributeDict(
                **{"triggered_inputs": [{"prop_id": "radios-base-currency-selector.value"}]}
            )
        )
        return barplot_profit_callback(base_currency=base_currency, granularity=granularity)

    ctx = copy_context()
    output = ctx.run(run_callback)
    assert isinstance(output, Figure)
    assert output.layout.yaxis["title"]["text"] == f"{base_currency.upper()} Profit"
