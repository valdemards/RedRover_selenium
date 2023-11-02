from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_registration_wait(driver):
    driver.get('https://victoretc.github.io/selenium_waits/')
    lending_text = driver.find_element(By.XPATH, "//h1").text
    assert lending_text == 'Практика с ожиданиями в Selenium'

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

    # loading_finish = wait.until(EC.invisibility_of_element((By.XPATH, "//div[@id = 'loader']")))
    success_message = driver.find_element(By.XPATH, "//p[@id = 'successMessage']").text
    print(success_message)
    assert success_message == 'Вы успешно зарегистрированы!'