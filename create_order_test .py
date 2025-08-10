import requests
import json

# Функция для создания заказа
def create_order(api_url, order_data):
    response = requests.post(api_url + "/orders", json=order_data)
    if response.status_code == 201:
        return response.json()['track_number']
    else:
        raise Exception(f"Error creating order: {response.status_code}, {response.text}")

# Функция для получения данных о заказе по треку
def get_order_by_track(api_url, track_number):
    response = requests.get(api_url + f"/orders/{track_number}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching order: {response.status_code}, {response.text}")

# Основной тест
def test_create_and_get_order(api_url, order_data):
    try:
        # Шаг 1: Создание заказа
        track_number = create_order(api_url, order_data)
        print(f"Created order with track number: {track_number}")

        # Шаг 2: Получение заказа по треку
        order_details = get_order_by_track(api_url, track_number)
        print(f"Order details: {json.dumps(order_details, indent=4)}")

        assert order_details['track_number'] == track_number, "Track number mismatch!"
        print("Test passed: Order details match.")
    except Exception as e:
        with open("/var/www/backend/logs/error.log", "a") as log_file:
            log_file.write(str(e) + "\n")
        print(f"Test failed: {str(e)}")

# Пример использования
if __name__ == "__main__":
    API_URL = https://a66cb31f-3317-428b-ae9e-c9d3cea5b84f.serverhub.praktikum-services.ru/"
    ORDER_DATA = {
        "product_id": 12345,
        "quantity": 2,
        "customer_id": 67890
    }

    test_create_and_get_order(API_URL, ORDER_DATA)
