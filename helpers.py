import requests
import random
import string
from data import courier_url, login_url, orders_url


def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass

def generate_courier_data():
    letters = string.ascii_lowercase
    return {
        'login': ''.join(random.choice(letters) for i in range(10)),
        'password': ''.join(random.choice(letters) for i in range(10)),
        'firstName': ''.join(random.choice(letters) for i in range(10))
        }

def create_courier(payload):
    return requests.post(courier_url, data=payload)

def login_courier(payload):
    return requests.post(login_url, data=payload)

def make_order(payload):
    return requests.post(orders_url, json=payload)

def get_order_list():
    return requests.get(orders_url)
 