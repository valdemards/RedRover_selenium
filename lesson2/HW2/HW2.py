import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time


# Authorization tests
def test_correct_login_form(driver):
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
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


#Cart tests
def test_add_to_cart_from_catalog(driver, logging):
    text_before = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div').text
    add_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_button.click()
    cart_button = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    cart_button.click()
    text_after = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div').text
    assert text_before == text_after


def test_remove_from_cart(driver, logging):
    add_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_button.click()
    cart_button = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    cart_button.click()
    remove_button = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')
    remove_button.click()
    try:
        deleted = False
        deleted_element = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div')
    except NoSuchElementException:
        deleted = True
    assert deleted


def test_add_to_cart_from_card(driver, logging):
    text_before = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div').text
    item_button = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
    item_button.click()
    add_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_button.click()
    cart_button = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    cart_button.click()
    text_after = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div').text
    assert text_before == text_after


def test_remove_from_cart_from_card(driver, logging):
    item_button = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
    item_button.click()
    add_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_button.click()
    remove_button = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')
    remove_button.click()
    cart_button = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    cart_button.click()
    try:
        deleted = False
        deleted_element = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div')
    except NoSuchElementException:
        deleted = True
    assert deleted


#Card tests
def test_card_image(driver, logging):
    item_image = driver.find_element(By.XPATH, '//a[@id="item_4_img_link"]/img')
    item_image.click()
    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"


def test_card_image(driver, logging):
    item_image = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
    item_image.click()
    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"


#Checkout tests
def test_checkout(driver, logging):
    add_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_button.click()
    cart_button = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    cart_button.click()
    checkout_button = driver.find_element(By.XPATH, '//button[@data-test="checkout"]')
    checkout_button.click()
    firstname_field = driver.find_element(By.XPATH, '//input[@data-test="firstName"]')
    firstname_field.send_keys("bob")
    lastname_field = driver.find_element(By.XPATH, '//input[@data-test="lastName"]')
    lastname_field.send_keys("loucas")
    zip_field = driver.find_element(By.XPATH, '//input[@data-test="postalCode"]')
    zip_field.send_keys("000007")
    continue_button = driver.find_element(By.XPATH, '//input[@data-test="continue"]')
    continue_button.click()
    finish_button = driver.find_element(By.XPATH, '//button[@data-test="finish"]')
    finish_button.click()
    text_after = driver.find_element(By.XPATH, '//div[@class="complete-text"]').text
    assert text_after == 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'


#Filter tests
def test_filter_az(driver, logging):
    filter_button = driver.find_element(By.XPATH, '//select[@class="product_sort_container"]')
    filter_button.click()
    filter_option = driver.find_element(By.XPATH, '//option[@value="az"]')
    filter_option.click()
    items = driver.find_elements(By.XPATH, '//div[@class="inventory_item_name "]')
    text_items = [item.text for item in items]
    sorted_items = sorted(text_items, reverse=False)
    assert text_items == sorted_items


def test_filter_za(driver, logging):
    filter_button = driver.find_element(By.XPATH, '//select[@class="product_sort_container"]')
    filter_button.click()
    filter_option = driver.find_element(By.XPATH, '//option[@value="za"]')
    filter_option.click()
    items = driver.find_elements(By.XPATH, '//div[@class="inventory_item_name "]')
    text_items = [item.text for item in items]
    sorted_items = sorted(text_items, reverse=True)
    assert text_items == sorted_items


def test_filter_lohi(driver, logging):
    filter_button = driver.find_element(By.XPATH, '//select[@class="product_sort_container"]')
    filter_button.click()
    filter_option = driver.find_element(By.XPATH, '//option[@value="lohi"]')
    filter_option.click()
    items = driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')
    text_items = [float(item.text.replace('$', '')) for item in items]
    sorted_items = sorted(text_items, reverse=False)
    assert text_items == sorted_items


def test_filter_hilo(driver, logging):
    filter_button = driver.find_element(By.XPATH, '//select[@class="product_sort_container"]')
    filter_button.click()
    filter_option = driver.find_element(By.XPATH, '//option[@value="hilo"]')
    filter_option.click()
    items = driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')
    text_items = [float(item.text.replace('$', '')) for item in items]
    sorted_items = sorted(text_items, reverse=True)
    assert text_items == sorted_items


#Burger menu tests
def test_logout(driver, logging):
    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(0.2)
    # logout = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
    logout = driver.find_element(By.XPATH, '//nav/a[@id="logout_sidebar_link"]')
    logout.click()
    assert driver.current_url == "https://www.saucedemo.com/"


def test_about(driver, logging):
    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(0.2)
    about = driver.find_element(By.XPATH, '//nav/a[@id="about_sidebar_link"]')
    about.click()
    assert driver.current_url == 'https://saucelabs.com/'


def test_reset(driver, logging):
    add_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_button.click()
    cart_button = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    cart_button.click()
    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(0.2)
    reset = driver.find_element(By.XPATH, '//nav/a[@id="reset_sidebar_link"]')
    reset.click()
    driver.refresh()
    try:
        deleted = False
        deleted_element = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div')
    except NoSuchElementException:
        deleted = True
    assert deleted


#Registration form tests
def test_checkbox(driver):
    driver.get('https://victoretc.github.io/webelements_information/')
    checkbox = driver.find_element(By.XPATH, '//input[@type="checkbox"]')
    checkbox.click()
    assert checkbox.is_selected()