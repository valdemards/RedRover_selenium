import pytest
from data import REGISTRATION_PAGE, LOGIN, PASSWORD
from locators import HEADER, START_TESTING_BUTTON, LOGIN_FIELD, PASSWORD_FIELD, AGREE_CHECKBOX, REGISTRATION_BUTTON, LOADER, SUCCESS_MESSAGE
from selenium.webdriver.support import expected_conditions as EC


def test_registration_positive(driver, wait):
    driver.get(REGISTRATION_PAGE)
    # header = driver.find_element(By.XPATH, "//h1").text
    header = driver.find_element(*HEADER).text
    assert header == 'Практика с ожиданиями в Selenium'

    start_button = wait.until(EC.element_to_be_clickable(START_TESTING_BUTTON))
    assert start_button.text == 'Начать тестирование'

    start_button.click()

    login_field = driver.find_element(*LOGIN_FIELD)
    login_field.clear()
    login_field.send_keys(LOGIN)

    password_field = driver.find_element(*PASSWORD_FIELD)
    password_field.clear()
    password_field.send_keys(PASSWORD)

    checkbox_agree = driver.find_element(*AGREE_CHECKBOX)
    checkbox_agree.click()
    assert checkbox_agree.is_selected()

    registration_button = driver.find_element(*REGISTRATION_BUTTON)
    registration_button.click()

    loader = wait.until(EC.visibility_of_element_located(LOADER))

    success_message = wait.until(EC.visibility_of_element_located(SUCCESS_MESSAGE))
    assert success_message.text == 'Вы успешно зарегистрированы!'
