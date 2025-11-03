import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Autorization import Autorization


@pytest.fixture
def driver():
    """Создание и закрытие браузера для каждого теста"""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    """Авторизация перед тестами"""
    page = Autorization(driver)
    page.click()
    page.login("эл_почта", "пароль")
    page.click_schedule()
    return driver
