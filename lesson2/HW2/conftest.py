import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Fixtures
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def logging(driver):
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()