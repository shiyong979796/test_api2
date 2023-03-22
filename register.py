from datetime import datetime
from common.handle_conf_file import base_url
import requests


def register(country=None):
    url = base_url + '1.0/user/register'
    str_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    email = 'outotest' + str_time + '@tetx.com'
    data = {"email": email, "password": "123456"}
    if country:
        headers = {"Content-Type": "application/json", "x-app": 'pc', "x-token": "",
                   "x-project": "azazie", "x-countryCode": country}
    else:
        headers = {"Content-Type": "application/json", "x-app": 'pc', "x-token": "",
                   "x-project": "azazie", "x-countryCode": 'us'}
    res = requests.post(url, json=data, headers=headers)
    return res.json()


if __name__ == '__main__':
    pass


