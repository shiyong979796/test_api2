import requests
from common.handle_log import log
from common.handle_conf_file import cf


def get_header(headers, token):
    if headers:
        if isinstance(headers, str):
            headers = eval(headers)
        elif token:
            headers['x-token'] = token
        return headers

    else:
        headers = {"Content-Type": "application/json", "x-app": 'pc', "x-token": "",
                   "x-project": "azazie", "x-countryCode": 'us'}
        return headers


def check_url(url):
    """
       拼接接口的url地址。
       """
    # base_url = cf.get_str("Url", "PROD_URL")
    # if url.startswith("/"):
    #     return base_url + url
    # else:
    return url


def send_request(method, url, data=None, headers=None, token=None, out_put=True):
    # url 处理
    url = check_url(url)

    # headers处理
    headers = get_header(headers, token)

    # 请求方式大写处理
    method = method.upper()

    log.info("请求头为：{}".format(headers))
    log.info("请求方法为：{}".format(method))
    log.info("请求url为：{}".format(url))
    log.info("请求数据为：{}".format(data))
    if isinstance(data, str):
        data = eval(data)

    if method == 'GET':
        res = requests.get(url, headers=headers)
        log.info('响应状态码为：({})'.format(res.status_code))
        if out_put:
            log.info('接口响应结果为：({})'.format(res.json()))
        return res
    elif method == 'POST':
        res = requests.post(url, json=data, headers=headers)
        log.info('响应状态码为：({})'.format(res.status_code))
        if out_put:
            log.info('接口响应结果为：({})'.format(res.json()))
        return res
    elif method == 'PUT':
        res = requests.put(url, json=data, headers=headers)
        log.info('响应状态码为：({})'.format(res.status_code))
        if out_put:
            log.info('接口响应结果为：({})'.format(res.json()))
        return res
    elif method == 'DELETE':
        res = requests.delete(url, json=data, headers=headers)
        log.info('响应状态码为：({})'.format(res.status_code))
        if out_put:
            log.info('接口响应结果为：({})'.format(res.json()))
        return res


if __name__ == '__main__':
    pass
