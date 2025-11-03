import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Schedule import SchedulePage


class Autorization:
    URL = "https://id.skyeng.ru/login"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Открываем страницу входа")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Выбираем авторизацию по почте")
    def click(self):
        self.open()

        self.wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Войти с помощью пароля")))

        email_button = self.driver.find_element(
            By.LINK_TEXT, "Войти с помощью пароля")
        email_button.click()

    @allure.step("Авторизация в личном кабинете")
    def login(self, email, password):
        self.click()
        email_field = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "username")))
        password_field = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "password")))

        email_field.send_keys(email)
        password_field.send_keys(password)

        login_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "span.js-username-password-form-button")))
        login_button.click()

    @allure.step("Переход во вкладку расписание")
    def click_schedule(self):
        # self.login(self, email, password)
        jump = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             "//div[contains(@class,'title') and normalize-space(text())='Расписание']")))
        jump.click()

        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "ds-icon[name='add']")))

        return SchedulePage(self.driver)
