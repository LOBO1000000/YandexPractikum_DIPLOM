# Глеб Филиппов, 27-я когорта — Финальный проект. Инженер по тестированию расширенный

import sender_stand_request

import data

# Автотест
def positive_assert():
    track_response = sender_stand_request.get_order(data.params_get)
    assert track_response.status_code == 200


def test_order():
    data.params_get["t"] = sender_stand_request.create_order()
    positive_assert()
