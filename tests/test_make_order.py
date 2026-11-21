import pytest 
import allure
from helpers import make_order
from data import order_data


@allure.suite('Создание заказа')
class TestOrder:

    @allure.title('Создание заказа с разными цветами возвращает код 201 и track')
    @pytest.mark.parametrize(
        'color',
        [
            ['BLACK'],
            ['GREY'],
            ['BLACK', 'GREY'],
            []
        ]
    )
    def test_make_order_with_different_colors_returns_201_and_track(self, color):
        payload = order_data.copy()
        payload['color'] = color

        response = make_order(payload)

        assert response.status_code == 201
        assert 'track' in response.json()
        assert isinstance(response.json()['track'], int)
 