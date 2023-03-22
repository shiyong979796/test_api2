import requests

headers1 = {"Content-Type": "application/json", "x-app": 'pc', "x-token": "",
            "x-project": "azazie", "x-countryCode": 'it', 'x-languageCode': 'it'}

headers2 = {"Content-Type": "application/json", "x-app": 'pc', "x-token": "",
            "x-project": "azazie", "x-countryCode": 'fr', 'x-languageCode': 'fr'}
fr_goods = []
it_goods = []
no_goods = []
no_it_goods = []

url ='https://p4.azazie.com/pre/1.0/list/content?cat_name=all-mom-and-celebration-dresses&dress_type=dress&page=1&limit=60&in_stock=&sort_by=popularity&is_outlet=0&version=b&activityVerison=a'
res = requests.post(url=url, headers=headers1)
goods_id = res.json()['data']['goodsIdList']

for goods in goods_id:
    it_goods.append(goods)

url = 'https://p4.azazie.com/pre/1.0/list/content?cat_name=all-mom-and-celebration-dresses&dress_type=dress&page=1&limit=60&in_stock=&sort_by=popularity&is_outlet=0&version=b&activityVerison=a'
res = requests.post(url=url, headers=headers2)
goods_info = res.json()['data']['goodsIdList']
for goods in goods_info:
    fr_goods.append(goods)

for i in it_goods:
    if i not in fr_goods:
        no_goods.append(i)

for i in fr_goods:
    if i not in it_goods:
        no_it_goods.append(i)
print('no_it_goods:',(no_it_goods))


print('it:', len(it_goods))
print('fr:', len(fr_goods))
print(len(set(fr_goods)))
print(len(set(it_goods)))
print(no_goods)
print(it_goods)


# print(fr_goods)
