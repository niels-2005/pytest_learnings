# conftest.py
import pytest


@pytest.fixture(scope="session")
def weekdays1():
    return ["mon", "tue", "wed"]


@pytest.fixture(scope="session")
def weekdays2():
    return ["fri", "sat", "sun"]


@pytest.fixture()
def setup01():
    def get_structure(name):
        if name == "list":
            return [1, 2, 3]
        elif name == "tuple":
            return (1, 2, 3)

    return get_structure
