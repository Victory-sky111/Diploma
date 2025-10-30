import allure
import requests

base_url = "https://api-teachers.skyeng.ru/v2/schedule/"
token = "token_global"
headers = {"Cookie": f"token_global={token}",
           "Content-Type": "application/json"}


@allure.story("Создание Личного события нажатием на слот")
def test_create_project():
    """Создание Личного события нажатием на слот"""
    with allure.step("Тело запроса"):
        payload = {"backgroundColor": "#F4F5F6",
                   "color": "#81888D",
                   "description": "",
                   "endAt": "2025-12-01T23:30:00+03:00",
                   "startAt": "2025-12-01T23:00:00+03:00",
                   "title": "Пробник"}
    with allure.step("Запрос"):
        response = requests.post(base_url + 'createPersonal',
                                 headers=headers, json=payload)
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200, f"Ошибка: {response.text}"
    with allure.step("Проверка созданного события"):
        data = response.json()
        id = data["data"]["payload"]["id"]
        assert "id" in data["data"]["payload"], f"Нет события {id} "
        return id


@allure.story("Изменение названия Личного события")
def test_update_title():
    """Изменение названия Личного события"""
    id = test_create_project()
    with allure.step("Тело запроса"):
        payload = {"backgroundColor": "#F4F5F6",
                   "color": "#81888D",
                   "description": "",
                   "endAt": "2025-12-01T23:30:00+03:00",
                   "id": id,
                   "oldStartAt": "2025-12-01T23:00:00+03:00",
                   "startAt": "2025-12-01T23:00:00+03:00",
                   "title": "Пробник новый"}
    with allure.step("Запрос"):
        response = requests.post(base_url + 'updatePersonal',
                                 headers=headers, json=payload)
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200
    with allure.step("Проверка изменений в названии события"):
        assert response.json()["data"]["payload"]["payload"]["title"]


@allure.story("Изменение даты Личного события")
def test_update_data():
    """Изменение даты Личного события"""
    id = test_create_project()
    with allure.step("Тело запроса"):
        payload = {"backgroundColor": "#F4F5F6",
                   "color": "#81888D",
                   "description": "",
                   "endAt": "2025-12-03T23:30:00+03:00",
                   "id": id,
                   "oldStartAt": "2025-12-01T23:00:00+03:00",
                   "startAt": "2025-12-03T23:00:00+03:00",
                   "title": "Пробник новый"}
    with allure.step("Запрос"):
        response = requests.post(base_url + 'updatePersonal',
                                 headers=headers, json=payload)
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200
    with allure.step("Проверка изменений даты"):
        assert response.json()["data"]["startAt"]


@allure.story("Удаление Личного события")
def test_delete():
    """Удаление Личного события"""
    id = test_create_project()
    with allure.step("Тело запроса"):
        payload = {"id": id,
                   "startAt": "2025-12-03T23:00:00+03:00"}
    with allure.step("Запрос на удаление"):
        response = requests.post(base_url + 'removePersonal',
                                 headers=headers, json=payload)
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200


@allure.story("Создание Личного события без названия")
def test_create_project_without_title():
    """Создание Личного события без названия"""
    with allure.step("Тело запроса"):
        payload = {"backgroundColor": "#F4F5F6",
                   "color": "#81888D",
                   "description": "",
                   "endAt": "2025-12-01T23:30:00+03:00",
                   "startAt": "2025-12-01T23:00:00+03:00"}
    with allure.step("Запрос"):
        response = requests.post(base_url + 'createPersonal',
                                 headers=headers, json=payload)
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200
        print("Field is required")
