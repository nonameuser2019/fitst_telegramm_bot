import requests
from setting import NEW_POST_TOKEN
HEADERS = {
    'Content-Type': 'application/json/'
}
tracking_number = '59000453739019'
client_phone = ''
documents = {
        'DocumentNumber': tracking_number,
        'Phone': client_phone
    }
URL = 'https://api.novaposhta.ua/v2.0/json/'
data = {
    "apiKey": NEW_POST_TOKEN,
    "modelName": "TrackingDocument",
    "calledMethod": "getStatusDocuments",
    "methodProperties": {
    "Documents": [
        documents
            ]
}
}


def get_api(URL, tracking_number):
    result = requests.post(URL, json=data, headers= HEADERS)
    if result.json()['success']:
        return f"Номер отслеживания посылки: {result.json()['data'][0]['Number']}\n" \
               f"Ожидаемая дата доставки {result.json()['data'][0]['ScheduledDeliveryDate']}\n" \
               f"Вес посылки: {result.json()['data'][0]['DocumentWeight']} кг.\n" \
               f"Стоимость доставки {result.json()['data'][0]['DocumentCost']} грн.\n" \
               f"Оплачивет доставку {result.json()['data'][0]['PayerType']}\n" \
               f"Маршрут {result.json()['data'][0]['CitySender']} - {result.json()['data'][0]['CityRecipient']}\n" \
               f"Адрес доставки: {result.json()['data'][0]['WarehouseRecipient']}\n" \



