import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchFrameException
from selenium.webdriver.chrome.service import Service as ChromeService
url = "https://firma-test.atochile.cl/sondacoreapp/login"
@pytest.fixture()

def setup():
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    driver.get(url)
    print("funciona")
    return driver



