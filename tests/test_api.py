import allure
import requests

base_url = "https://api-teachers.skyeng.ru/v2/schedule/"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjE0NzIwMDY5LCJpZGVudGl0eSI6InRlc3QudHN0MzIwQHNreWVuZy5ydSIsImlkZW50aXR5TG9naW4iOm51bGwsImlkZW50aXR5RW1haWwiOiJ0ZXN0LnRzdDMyMEBza3llbmcucnUiLCJpZGVudGl0eVBob25lIjoiKzc5ODU0NTg2NTY4IiwibmFtZSI6InRlc3RURUNUIiwic3VybmFtZSI6bnVsbCwiZW1haWwiOiJ0ZXN0LnRzdDMyMEBza3llbmcucnUiLCJ1aUxhbmd1YWdlIjoicnUiLCJsb2NhbGUiOiJydSIsInNlcnZpY2VMb2NhbGUiOm51bGwsInVhcyI6MzAsImp3dFR5cGUiOjEsImp0aSI6IjVsT1d4dzFFUWhHbmxhaWVDQ3NDS3hjWXpLS0pwTTNaIiwiYnJhbmQiOm51bGwsImV4cCI6MTc2MTk0NTIxMiwiYmlydGhkYXkiOiIyMDA3LTEyLTI4IiwiYUlzU3Ryb25nIjp0cnVlLCJhVHlwZSI6IlVTRVJOQU1FX1BBU1NXT1JEIiwiYVRpbWUiOjE3NjE2ODc2MDUsInJvbGVzIjpbIlJPTEVfVEVBQ0hFUl9DQU5ESURBVEUiLCJST0xFX1RFQUNIRVJfQ0FORElEQVRFX0JBU0VfQUNDRVNTIiwiUk9MRV9UUk1fVVBMT0FEX0ZJTEUiLCJST0xFX1RUQ19VU0FHRSIsIlJPTEVfVklNQk9YX1RFQUNIRVJfVVNBR0UiLCJST0xFX1RFQUNIRVIiLCJST0xFX0NSTTJfVEVBQ0hFUl9BQ0NFU1MiLCJST0xFX1RFQUNIRVJTX0NBQklORVRfQkFTRV9BQ0NFU1MiLCJST0xFX01BVEhfVEVBQ0hFUiIsIlJPTEVfTUFUSF9DT05URU5UX1RIRU1FX1ZJRVciXX0.iUQB1Qshy5eNK2U-mgUa9jg7R7p3GTTya6gosM2MqlGoFxncu8wEzf4idF5nYFWRDQNLpqFGe4aaBc7jUokIawR6EwMDZuRuBlZs4Euhe5RhO0VvPkvB0DSMRxxuvlPbPxnffQ1BjhRMJbX3YHVsg8BRNcI-tn7uDWxVc7aW-mGcn4HxCzH4L0iV2TnUo0Pijb7D9kKTbEBABdofR7MhlsOh2FPIam2ff5Uqk0JGkmz0sQcMebWRa7xePdM_qIVcQr9JXdSczjhetMurSz84u5uZMuLShxr80iA_sl3fUfxq12JYRmeYsrKIzO3LGkqXkBL4L5GKPHIahUb2tATVWol5luTvOSXLcLlxPJb0AEqJzLo8aWvlNvKp96P7ckscUExB8ZdwfxBbgQt5hPs1V2bGt3omalb0FIzg3vs3g1IhZMfPjF0W0c9Ms02t125XWepDk6Wr1pqzJKzdIvK_sexGwe2-xcEYWzLjW8mkNIlLgcWRu8CzTk-w7h0riOgo6wAEsAzucvlAjecsuoRra6O4hHoPC1ic2xBoBYXcGVBoNd0cqm9YJlUrrkF37gOO7f9WEcVWy7p2YFTQBTD0iMZe7m70nm1fNzhUEj8dR2f2uL7G2VIT1muAPB9MqBkJSeEvzEg-Wx4nEhKWh2G_TTCpPXyaqRQfYBusS0_Nm6k"
headers = {"Cookie": f"token_global={token}",
           "Content-Type": "application/json"}


@allure.story("Создание Личного события нажатиев на слот")
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
