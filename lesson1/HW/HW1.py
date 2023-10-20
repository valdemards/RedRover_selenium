import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def logging():
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()


def test_correct_login_form(driver):
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_not_correct_login_form(driver):
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("user")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    error = driver.find_element(By.XPATH, '//h3[@data-test="error"]').text
    time.sleep(1)
    assert error == 'Epic sadface: Username and password do not match any user in this service'


def test_add_to_cart(driver, logging):
    text_before = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div').text
    add_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_button.click()
    cart_button = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    cart_button.click()
    text_after = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div').text
    assert text_before == text_after


def test_remove_from_cart(driver, logging):
    text_before = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div').text
    remove_button = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')
    remove_button.click()
    text_after = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div').text
    assert text_before != text_after


def test_logout(driver, logging):
    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(1)
    # logout = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
    logout = driver.find_element(By.XPATH, '//nav/a[@id="logout_sidebar_link"]')
    logout.click()
    time.sleep(1)
    url_after = driver.current_url
    assert url_after == "https://www.saucedemo.com/"

