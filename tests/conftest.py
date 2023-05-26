import os

import pytest


def pytest_configure(config):
    config.addinivalue_line("markers", "no_env_var: mark test to not use env var mock")


@pytest.fixture(autouse=True)
def mock_env_variables(request):
    if not request.node.get_closest_marker("no_profiling"):
        os.environ['ROBOTHOOD_DB_PATH'] = ""
    yield
