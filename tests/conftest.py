import time
import pytest
from src.TestProject.sdk.drivers import web driver
@pytest.fixture
def driver():
    "creates a webdriver and loads the homepage"
    driver = webdriver.Chrome()
    driver.get("https://waylonwalker.com/")
    yield driver
    driver.quit()