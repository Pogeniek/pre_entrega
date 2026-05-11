# Configuracion del driver

import pytest
from selenium import webdriver
from utils.LoginPage import login


@pytest.fixture
def driver():
    option = webdriver.FirefoxOptions()
    option.add_argument("--incognito")

    driver = webdriver.Firefox(options= option)

    yield driver

    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver


