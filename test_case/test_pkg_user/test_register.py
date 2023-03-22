import pytest

from datetime import datetime

from common.handle_log import log
from test_case.test_pkg_user.get_register_case import register_case_data
from common.handle_conf_file import base_url
from common.handle_request import send_request
from common.handle_data import replace_all_data, GlobalVar, get_res_data


class TestRegister:

    def setup(self):
        log.info('\nstart run (test_register) case')
        email = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S') + '@tetx.com'
        setattr(GlobalVar, 'email', email)

    @pytest.mark.parametrize('case', register_case_data)
    def test_register(self, case):
        # 数据替换
        case = replace_all_data(case)

        res = send_request(case['method'], base_url + case['url'], case['data'], headers=case['header'])
        if case['extract']:
            get_res_data(res.json(), case['extract'], case['case_name'])
        pytest.assume(eval(case['expect'])['code'] == res.json()['code'])


class TestDemo:
    def setup(self):  # 方法前置
        pass

    def teardown(self):  # 方法后置
        pass
