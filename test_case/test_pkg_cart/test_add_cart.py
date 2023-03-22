from common.handle_request import send_request
from test_case.test_pkg_cart.get_add_cart_case import add_cart_case_data
from common.handle_log import log
from mypath import prime_data_dir
from common.handle_csv import handle_cart_data
from common.handle_conf_file import base_url
import pytest
import os


class TestAddCart:
    @pytest.mark.usefixtures('cart_login')
    @pytest.mark.parametrize('case', add_cart_case_data)
    def test_add_cart(self, cart_login, case):
        # 数据替换

        case = handle_cart_data(os.path.join(prime_data_dir, case['mark']), case)
        log.info('case data 为：{}'.format(case))
        # 调用加车接口
        res = send_request(case['method'], base_url + case['url'], case['data'], headers=case['header'])

        assert res.json()['code'] == eval(case['expected'])['code']
        assert res.json()['msg'] == eval(case['expected'])['msg']

