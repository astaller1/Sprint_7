import pytest
import allure
from helpers import login_courier, generate_courier_data


@allure.suite('Логин курьера')
class TestCourierLogin:

    @allure.title('Успешная авторизация курьера возвращает код 200 и id')
    def test_courier_successfull_login(self, registered_courier):
        login, password, first_name = registered_courier
        payload = {
            'login': login,
            'password': password
            }
        response = login_courier(payload)

        assert response.status_code == 200
        assert 'id' in response.json()
        assert isinstance(response.json()['id'], int)

    @allure.title('Авторизация без обязательного поля возвращает 400 Bad Request')
    @pytest.mark.parametrize('empty_required_input', ['login', 'password'])
    def test_login_without_required_field_returns_400(self, empty_required_input, registered_courier):
        login, password, first_name = registered_courier
        payload = {
            'login': login,
            'password': password
            }
        del payload[empty_required_input]

        response = login_courier(payload)

        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Авторизация с неверным логином или паролем возвращает ошибку 404 Not Found')
    @pytest.mark.parametrize('wrong_input', ['login', 'password'])
    def test_login_with_wrong_required_field_returns_404(self, wrong_input, registered_courier):
        login, password, first_name = registered_courier
        payload = {
            'login': login,
            'password': password
            }
        payload[wrong_input] = f'wrong_{payload[wrong_input]}'

        response = login_courier(payload)

        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"

    @allure.title('Авторизация под несуществующим пользователем возвращает ошибку 404 Not Found')
    def test_login_nonexistent_courier_returns_404(self):
        random_data = generate_courier_data()
        payload = {
            'login': random_data['login'],
            'password': random_data['password']
            }

        response = login_courier(payload)

        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"
 