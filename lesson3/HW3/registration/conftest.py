from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import pytest



@pytest.fixture()
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options


@pytest.fixture()
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    return driver


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, timeout=7)
    return wait