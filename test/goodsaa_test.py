import requests
he = {"Content-Type": "application/json", "x-app": 'pc', "x-token": "",
                        "x-project": "azazie", "x-countryCode": 'us'}
url = "https://apix-p3.azazie.com/1.0/list/content?cat_name=bridesmaid-dresses&dress_type=dress&page=1&limit=30&version=b&activityVerison=a"
res =requests.post(url=url,headers=he)
print(res.json()['data']['goodsIdList'][0:10])