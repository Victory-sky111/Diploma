import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SchedulePage:
    URL = "https://teachers.skyeng.ru/schedule"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Открываем страницу расписания")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Создание личного события")
    def create_event(self, title, description=""):
        self.open()
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "ds-icon[name='add']"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             "//span[contains(@class,'text-center') and normalize-space(text()) = 'Личное событие']"))).click()

        name_input = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Например: посмотреть вебинар']")))
        name_input.send_keys(title)

        if description:
            desc = self.driver.find_element(
                By.CSS_SELECTOR,
                "textarea[placeholder='Например: ссылка на вебинар']")
            desc.send_keys(description)

        self.driver.find_element(
            By.XPATH, "//div[normalize-space(text())='Cохранить']").click()
        self.wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, f"//div[contains(@class,'long-view__title')"
             f"and text()='{title}'][last()]"), title))

    @allure.step("Изменение даты личного события")
    def change_event_date(self, title, new_date="6 ноября"):
        self.open()
        event = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[contains(@class,'long-view__title')"
             f"and text()='{title}'][last()]")))
        event.click()

        date_dropdown = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[text()=' Редактировать ']")))
        date_dropdown.click()
        option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//select[contains(@class,'class-date')]/"
             f"option[normalize-space(text())='{new_date}']")))
        option.click()

        self.driver.find_element(
            By.XPATH, "//div[normalize-space(text())='Cохранить']").click()
        self.wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, f"//div[contains(@class,'long-view__title')"
             f"and text()='{title}'][last()]"), title))

    @allure.step("Удаление личного события")
    def delete_event(self, title):
        self.open()
        event = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[contains(@class,'long-view__title')"
             f"and text()='{title}'][last()]")))
        event.click()

        delete_evt = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[contains(@class,'text-container')"
             f"and normalize-space(text())='Удалить']")))
        delete_evt.click()

    @allure.step("Создание личного события без названия")
    def try_save_empty_event(self):
        self.open()
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "ds-icon[name='add']"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(@class,'text-center') and normalize-space(text())='Личное событие']"))).click()

        save_button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[text()=' Cохранить ']")))
        if not save_button.is_enabled():
            return "disabled"
        else:
            save_button.click()
            return "enabled"

    @allure.step("Проверка наличия цветов при создании события")
    def count_colors(self):
        self.open()
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "ds-icon[name='add']"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             "//span[contains(@class,'text-center') and normalize-space(text()) = 'Личное событие']"))).click()
        colors = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@class, 'color-circle')]")))
        return len(colors)
