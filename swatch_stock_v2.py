import requests


url = 'http://common-prod.opsfun.com/stock/v2/goodsId?warehouse=10&business_id=65582&goods_id=1000291'


# headers = {"Content-Type": "application/json", "x-app": 'pc', "x-token": "",
#                    "x-project": "azazie", "x-countryCode": 'us'}
def get_stock():
    res = requests.get(url)
    count = 0
    for i in res.json()['data']['1000291']:
        if i['available_quantity'] != 0:
            count += 1
            print(i['sku'],i['available_quantity'])
    print(count)


def get_no_stock():
    res = requests.get(url)
    count = 0
    for i in res.json()['data']['1000291']:
        if i['available_quantity'] == 0:
            print(i['sku'], i['available_quantity'])
    print(count)


get_no_stock()