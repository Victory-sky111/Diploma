import requests

base_url = "https://api-teachers.skyeng.ru/v2/schedule/"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjE0NzIwMDY5LCJpZGVudGl0eSI6InRlc3QudHN0MzIwQHNreWVuZy5ydSIsImlkZW50aXR5TG9naW4iOm51bGwsImlkZW50aXR5RW1haWwiOiJ0ZXN0LnRzdDMyMEBza3llbmcucnUiLCJpZGVudGl0eVBob25lIjoiKzc5ODU0NTg2NTY4IiwibmFtZSI6InRlc3RURUNUIiwic3VybmFtZSI6bnVsbCwiZW1haWwiOiJ0ZXN0LnRzdDMyMEBza3llbmcucnUiLCJ1aUxhbmd1YWdlIjoicnUiLCJsb2NhbGUiOiJydSIsInNlcnZpY2VMb2NhbGUiOm51bGwsInVhcyI6MzAsImp3dFR5cGUiOjEsImp0aSI6ImtFeHBpcGxDbDBGVXExQmRLY0tRbVVhUmlGRng1MHk5IiwiYnJhbmQiOm51bGwsImV4cCI6MTc2MTc3NDAxMCwiYmlydGhkYXkiOiIyMDA3LTEyLTI4IiwiYUlzU3Ryb25nIjp0cnVlLCJhVHlwZSI6IlVTRVJOQU1FX1BBU1NXT1JEIiwiYVRpbWUiOjE3NjE2ODc2MDUsInJvbGVzIjpbIlJPTEVfVEVBQ0hFUl9DQU5ESURBVEUiLCJST0xFX1RFQUNIRVJfQ0FORElEQVRFX0JBU0VfQUNDRVNTIiwiUk9MRV9UUk1fVVBMT0FEX0ZJTEUiLCJST0xFX1RUQ19VU0FHRSIsIlJPTEVfVklNQk9YX1RFQUNIRVJfVVNBR0UiLCJST0xFX1RFQUNIRVIiLCJST0xFX0NSTTJfVEVBQ0hFUl9BQ0NFU1MiLCJST0xFX1RFQUNIRVJTX0NBQklORVRfQkFTRV9BQ0NFU1MiLCJST0xFX01BVEhfVEVBQ0hFUiIsIlJPTEVfTUFUSF9DT05URU5UX1RIRU1FX1ZJRVciXX0.APbuTc44UML0eE4oRSywQOwKKiUnBojlYN2-IRTZn1bwPBe9njLPtYoFYlywDsQGRLsl1sFsQvndvWbmMvIq2iNOVmexBObIG-9ZzijgkXzWt_aP8Rd9k_TPsP6XIleL1WBkYfvIqZFaI6r8CowIPG1fK7cXIYH2SpThMrnDkywjtoGqwLS26tQqyQEpz6-2Dow4d7_uAvgTzq3e2Bc3e7M3ClZQAk8zoAMvdGl6KW2rfncEsYBOX3hF0_iWHfqf5DiEhM03yrJwIJfrBdj66GdKU6pDD0XB-cYLIddVhMieUM2CAZkw6HBbkcMcNTKLVvngQS21eG_1GNY9c5R6wyGUyhHBzolX_WHOqE6VZ8zDas6biG_SCKZg4I2ajkVoM52toqyFxrB5mJdYo_rDW_333ubfBinDvUaCDUHe_wJFPVqta5NTUWk6lNjlqSvhqq0w5zTl-eYGAWAw4Imps8Q-gc6qp3rmhxnsg9a9Do_O4XFw5onyMUseuOZUavxC1G0YSY82rN0humC_al8NuBT_g7-NlsjS8NI30qXlSwXM-Z-fV34eoXJj8fwW_SvLzRQLuuqO8ocIILZVPquRqmPxafI9ZEtpCdPho60YzkYUHD1hpFWh7Zc754ckvedy7QTSTeSC4ieNEePnTskHPcel1CUVHw4UFR6mcy-Irxc"
headers = {"Cookie": f"token_global={token}", "Content-Type": "application/json"}


def test_create_project():
    """Создание Личного события нажатием на слот"""
    payload = {"backgroundColor": "#F4F5F6",
               "color": "#81888D",
               "description": "",
               "endAt": "2025-12-01T23:30:00+03:00",
               "startAt": "2025-12-01T23:00:00+03:00",
               "title": "Пробник"}
    response = requests.post(base_url + 'createPersonal', headers=headers, json=payload)
    assert response.status_code == 200, f"Ошибка: {response.text}"
    data = response.json()
    assert "data" in data, f"Нет 'data' в ответе: {data}"
    assert "payload" in data["data"], f"Нет 'payload' в data: {data['data']}"
    assert "id" in data["data"]["payload"], f"Нет 'id' в data: {data['data']["payload"]}"

def test_update_name():
    """Изменение навзвания Личного события"""


def test_update_name():
    """Изменение названия Личного события"""


def test_update_color():
    """Изменение цвета Личного события"""

def test_update_color():
    """Удаление Личного события"""

def test_update_color():
    """Создание Личного события без названия"""
