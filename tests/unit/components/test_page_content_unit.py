import os
from contextvars import copy_context

import pytest
from dash._callback_context import context_value
from dash._utils import AttributeDict
from plotly.graph_objs import Figure

from robothoodash.components.page_content import lineplot_base_currency_balance_callback
from robothoodash.hoodapi.hoodapi import ALLOWED_BASE_CURRENCY


@pytest.mark.parametrize("base_currency", ALLOWED_BASE_CURRENCY, ids=ALLOWED_BASE_CURRENCY)
def test_lineplot_base_currency_balance_callback(
    mock_duckdb_connection, mock_env_variables, base_currency
):  # pylint:disable=unused-argument
    os.environ["ROBOTHOOD_DB_PATH"] = ""

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
