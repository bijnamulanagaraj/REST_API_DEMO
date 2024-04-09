import pytest
from pageObjects.api import Test_api
@pytest.fixture()
def test_api():
    base_url = "https://reqres.in"
    return Test_api(base_url)

