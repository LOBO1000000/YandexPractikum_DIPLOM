import configuration

import requests

import data

# создание заказа
def create_order():
    order_response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
    json=data.order_body)
    return order_response.json().get("track")

# Запрос на получение заказа по треку заказа
def get_order(track_order):
    return requests.get(configuration.URL_SERVICE+configuration.PUT_ORDER,
                        params=track_order)