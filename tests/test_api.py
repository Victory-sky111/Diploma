import allure
import requests

base_url = "https://api-teachers.skyeng.ru/v2/schedule/"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9." \
    "eyJ1c2VySWQiOjE0NzIwMDY5LCJpZGVudGl0eSI6InRlc3QudHN0MzIwQHNreWVuZ" \
    "y5ydSIsImlkZW50aXR5TG9naW4iOm51bGwsImlkZW50aXR5RW1haWwiOiJ0ZXN0LnRzdD" \
    "MyMEBza3llbmcucnUiLCJpZGVudGl0eVBob25lIjoiKzc5ODU0NTg2NTY4IiwibmFtZSI" \
    "6InRlc3RURUNUIiwic3VybmFtZSI6bnVsbCwiZW1haWwiOiJ0ZXN0LnRzdDMyMEBza3ll" \
    "bmcucnUiLCJ1aUxhbmd1YWdlIjoicnUiLCJsb2NhbGUiOiJydSIsInNlcnZpY2VMb2Nh" \
    "bGUiOm51bGwsInVhcyI6MzAsImp3dFR5cGUiOjEsImp0aSI6Ikx4bDJRMjN6V0VjSlU4" \
    "M3JVNjduVG5JMUJvRWFaUGhGIiwiYnJhbmQiOm51bGwsImV4cCI6MTc2MTg1NjgxMiwiY" \
    "mlydGhkYXkiOiIyMDA3LTEyLTI4IiwiYUlzU3Ryb25nIjp0cnVlLCJhVHlwZSI6IlVTRVJ" \
    "OQU1FX1BBU1NXT1JEIiwiYVRpbWUiOjE3NjE2ODc2MDUsInJvbGVzIjpbIlJPTEVfVEVBQ0" \
    "hFUl9DQU5ESURBVEUiLCJST0xFX1RFQUNIRVJfQ0FORElEQVRFX0JBU0VfQUNDRVNTIiwi" \
    "Uk9MRV9UUk1fVVBMT0FEX0ZJTEUiLCJST0xFX1RUQ19VU0FHRSIsIlJPTEVfVklNQk9YX1R" \
    "FQUNIRVJfVVNBR0UiLCJST0xFX1RFQUNIRVIiLCJST0xF" \
    "X0NSTTJfVEVBQ0hFUl9BQ0NFU1M" \
    "iLCJST0xFX1RFQUNIRVJTX0NBQklORVRfQkFTRV9BQ0NFU1MiLCJST0xFX01BVEhfVEVBQ0" \
    "hFUiIsIlJPTEVfTUFUSF9DT05URU5UX1RIRU1FX1ZJRVciXX0.2bC3pvD1qoVET9L2teos6" \
    "vyY1HafhEnus-Pi9-L1D77Cla8bLTE1F5pl6IiairbY7Sk-sX5AO" \
    "imoRb7CXvx4k6uglpHoR" \
    "IfdwrmGwMsJ-D9kOOxf9b9EhPQ-1oGTvhzB7Z" \
    "V3pfpHTQOGMrRMK_aW5dM45OGnK_zr-Z0xq" \
    "yG6wv8zXO2CGIVqCosqkSKjxj6D74MPnrLVjt_5MER6ASGFoZPzImNTLvthFKWc" \
    "x5UqjSxsECO" \
    "Y92j1MWWLRqmg4mrNoQgigRKL6yJiP6iljSwNohXtYDUELwccB8D_26BZXekx_dI0CFG4H" \
    "jqkV-6OMxlAMK35kKWpGrgaKUwn374b-XZXGdUKFt0" \
    "mAorGVYkpthfjuVX0YqXr-PUEdbzmq" \
    "DHq8M4PPW1gH39azCE1zo844DOZcxmNOJXOlDDkcK9" \
    "99Ax0v8W_KOVhQXbowR-BdUI-Ak9VVb" \
    "gBGcwG8igqd9pmZUHkk9gVsQzi3irLsxj5R5VY6WtlfMWnHCLSWmFv2IZ4UDYTv" \
    "jf-8gD_i-URRBdTpbshP0aZhCEZ8OQe-LpZtYZ6Al-r2r6IKq-ImiqmHYJaMCZ0-ve71s" \
    "dOW8bK1nHZBeETpIT8wreKyS8sx71whQEyniXOfI1Vi01YJzKd-fRfkjDkOLh6iysovjk" \
    "RWyTRrJdJHiFDTqLnAQ0y6mgBQyM"
headers = {"Cookie": f"token_global={token}",
           "Content-Type": "application/json"}


@allure.story("Создание Личного события нажатиев на слот")
def test_create_project():
    """Создание Личного события нажатием на слот"""
    payload = {"backgroundColor": "#F4F5F6",
               "color": "#81888D",
               "description": "",
               "endAt": "2025-12-01T23:30:00+03:00",
               "startAt": "2025-12-01T23:00:00+03:00",
               "title": "Пробник"}
    response = requests.post(base_url + 'createPersonal',
                             headers=headers, json=payload)
    assert response.status_code == 200, f"Ошибка: {response.text}"
    data = response.json()
    id = data["data"]["payload"]["id"]
    # assert "data" in data, f"Нет 'data' в ответе: {data}"
    # assert "payload" in data["data"], f"Нет 'payload' в data: {data['data']}"
    # assert "id" in data["data"]["payload"], f"Нет 'id' в data: {
    # data['data']["payload"]}"
    assert "id" in data["data"]["payload"], f"Нет события {id} "
    # id = data["data"]["payload"]["id"]
    return id


@allure.story("Изменение названия Личного события")
def test_update_title():
    """Изменение названия Личного события"""
    id = test_create_project()
    payload = {"backgroundColor": "#F4F5F6",
               "color": "#81888D",
               "description": "",
               "endAt": "2025-12-01T23:30:00+03:00",
               "id": id,
               "oldStartAt": "2025-12-01T23:00:00+03:00",
               "startAt": "2025-12-01T23:00:00+03:00",
               "title": "Пробник новый"}
    response = requests.post(base_url + 'updatePersonal',
                             headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["data"]["payload"]["payload"]["title"]


@allure.story("Изменение даты Личного события")
def test_update_color():
    """Изменение даты Личного события"""
    id = test_create_project()
    payload = {"backgroundColor": "#F4F5F6",
               "color": "#81888D",
               "description": "",
               "endAt": "2025-12-03T23:30:00+03:00",
               "id": id,
               "oldStartAt": "2025-12-01T23:00:00+03:00",
               "startAt": "2025-12-03T23:00:00+03:00",
               "title": "Пробник новый"}
    response = requests.post(base_url + 'updatePersonal',
                             headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["data"]["startAt"]


@allure.story("Удаление Личного события")
def test_delete():
    """Удаление Личного события"""
    id = test_create_project()
    payload = {"id": id,
               "startAt": "2025-12-03T23:00:00+03:00"}
    response = requests.post(base_url + 'removePersonal',
                             headers=headers, json=payload)
    assert response.status_code == 200


@allure.story("Создание Личного события без названия")
def test_create_project_without_title():
    """Создание Личного события без названия"""
    payload = {"backgroundColor": "#F4F5F6",
               "color": "#81888D",
               "description": "",
               "endAt": "2025-12-01T23:30:00+03:00",
               "startAt": "2025-12-01T23:00:00+03:00"
               }
    response = requests.post(base_url + 'createPersonal',
                             headers=headers, json=payload)
    assert response.status_code == 200
    print("Field is required")
