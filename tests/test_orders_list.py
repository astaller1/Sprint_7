import pytest 
import allure
from helpers import get_order_list


@allure.suite('Список заказов')
class TestOrderList:

    @allure.title('Получение списка заказов возвращает код 200, в теле ответа список заказов')
    def test_get_orders_returns_order_list_and_200(self):
        response = get_order_list()

        assert response.status_code == 200
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)
 