from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
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


def test_registration(driver):
    driver.get('https://victoretc.github.io/selenium_waits/')
    lending_text = driver.find_element(By.XPATH, "//h1").text
    assert lending_text == 'Практика с ожиданиями в Selenium'

    time.sleep(5)
    start_button = driver.find_element(By.XPATH, "//button[@id = 'startTest']")
    assert start_button.text == 'Начать тестирование'
    start_button.click()

    login_field = driver.find_element(By.XPATH, "//input[@id='login']")
    login_field.send_keys('login')

    password_field = driver.find_element(By.XPATH, "//input[@id='password']")
    password_field.send_keys('password')

    checkbox = driver.find_element(By.XPATH, "//input[@id = 'agree']")
    checkbox.click()

    login_button = driver.find_element(By.XPATH, "//button[@id = 'register']")
    login_button.click()

    loader = driver.find_element(By.XPATH, "//div[@id = 'loader']")
    assert loader.is_displayed()

    time.sleep(4)
    success_message = driver.find_element(By.XPATH, "//p[@id = 'successMessage']").text
    assert success_message == 'Вы успешно зарегистрированы!'