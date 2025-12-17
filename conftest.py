import pytest
import allure
from selenium import webdriver
from curl import *

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(main_site)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(main_site)
    yield driver
    driver.quit()

@pytest.fixture
def test_credentials():
    return {
    "email": "gordy82@yandex.ru",
    "password": "5h235jq1!"
    }