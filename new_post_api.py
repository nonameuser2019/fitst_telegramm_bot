import requests
from setting import NEW_POST_TOKEN
HEADERS = {
    'Content-Type': 'application/json/'
}
URL = 'https://api.novaposhta.ua/v2.0/json/'


def get_api(URL, tracking_number):
    documents = {
        'DocumentNumber': tracking_number
    }

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

    result = requests.post(URL, json=data, headers= HEADERS)
    if result.json()['success']:
        return f"Номер отслеживания посылки: {result.json()['data'][0]['Number']}\n" \
               f"Ожидаемая дата доставки {result.json()['data'][0]['ScheduledDeliveryDate']}\n" \
               f"Вес посылки: {result.json()['data'][0]['DocumentWeight']} кг.\n" \
               f"Стоимость доставки {result.json()['data'][0]['DocumentCost']} грн.\n" \
               f"Маршрут {result.json()['data'][0]['CitySender']} - {result.json()['data'][0]['CityRecipient']}\n" \
               f"Адрес доставки: {result.json()['data'][0]['WarehouseRecipient']}\n" \

def main():
    info = get_api(URL, '59000453739019')
    print(info)


if __name__ == '__main__':
    main()

