import pytest
from copper_sdk import COPPER_API_TOKEN, COPPER_API_EMAIL
from copper_sdk.copper import Copper

@pytest.fixture(scope='session')
def copper():
    return Copper(COPPER_API_TOKEN, COPPER_API_EMAIL)
