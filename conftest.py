import pytest
import requests
from data import courier_url
from helpers import register_new_courier_and_return_login_password, generate_courier_data, login_courier


def delete_courier(login, password):
    login_response = login_courier({'login': login, 'password': password})
    if login_response.status_code != 200:
        return
    courier_id = login_response.json().get('id')
    if courier_id:
        requests.delete(f'{courier_url}/{courier_id}')

@pytest.fixture
def registered_courier():
    login, password, first_name = register_new_courier_and_return_login_password()
    yield login, password, first_name
    delete_courier(login, password)

@pytest.fixture
def courier_payload():
    payload = generate_courier_data()
    yield payload
    if 'login' in payload and 'password' in payload:
        delete_courier(payload['login'], payload['password'])
 