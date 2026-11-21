import pytest
import allure
from helpers import create_courier


@allure.suite('Создание курьера')
class TestCreateNewCourier:

    @allure.title('Успешное создание курьера возвращает код 201 и тело "ok: true"')
    def test_create_new_courier_successfull(self, courier_payload):
        response = create_courier(courier_payload)
        
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Регистрация курьера с уже существующими данными возвращает 409 Conflict')
    def test_create_existing_courier_returns_409(self, registered_courier):
        login, password, first_name = registered_courier
        payload = {
            'login': login,
            'password': password,
            'firstName': first_name
            }

        response = create_courier(payload)

        assert response.status_code == 409
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Регистрация курьера с уже существующим логином и неповторяющимся паролем возвращает 409 Conflict')
    def test_create_courier_with_existing_login_returns_409(self, registered_courier):
        existing_login, _, _ = registered_courier
        payload = {
            'login': existing_login,
            'password': 'new_password_123',
            'firstName': 'НовоеИмя'
        }

        response = create_courier(payload)

        assert response.status_code == 409
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."

    @allure.title ('Запрос без заполнения обязательного поля возвращает 400 Bad Request')
    @pytest.mark.parametrize('empty_required_input', ['login', 'password'])
    def test_create_courier_without_required_field_returns_400(self, empty_required_input, courier_payload):
        del courier_payload[empty_required_input]

        response = create_courier(courier_payload)

        assert response.status_code == 400
        assert response.json()['message'] ==  "Недостаточно данных для создания учетной записи"
 