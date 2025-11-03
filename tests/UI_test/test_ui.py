import allure
from Schedule import SchedulePage


@allure.story("Создание личного события")
def test_create_event(logged_in_driver):
    page = SchedulePage(logged_in_driver)
    page.create_event("Пробное событие", "важная информация")


@allure.story("Изменение даты события")
def test_change_event_date(logged_in_driver):
    page = SchedulePage(logged_in_driver)
    title = "Событие для смены даты"
    page.create_event(title)
    page.change_event_date(title, "Четверг, 6 ноября")


@allure.story("Проверка удаления события")
def test_delete_event(logged_in_driver):
    page = SchedulePage(logged_in_driver)
    title = "Событие для удаления"
    page.create_event(title)
    page.delete_event(title)


@allure.story("Создание события без названия")
def test_create_event_without_title(logged_in_driver):
    page = SchedulePage(logged_in_driver)
    result = page.try_save_empty_event()
    if result == "disabled":
        assert True, "Кнопка 'Сохранить' не активна"
    else:
        assert result != "closed", "Окно закрылось — событие создалось!"


@allure.story("Проверка наличия цветов при создании события")
def test_event_colors(logged_in_driver):
    page = SchedulePage(logged_in_driver)
    count = page.count_colors()
    print(f"Количество доступных цветов: {count}")
    assert count == 4, f"Ожидалось 4 цвета, фактически {count}"
