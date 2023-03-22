import re
from jsonpath import jsonpath

from common.handle_conf_file import cf
from common.handle_log import log


class GlobalVar:
    pass


def get_res_data(res, extract_item, case_name):
    log.info('case {} 提取参数({})'.format(case_name, extract_item))
    for key, value in eval(extract_item).items():
        extract_value = jsonpath(res, value)[0]
        setattr(GlobalVar, key, extract_value)


def replace_all_data(case):
    """
    遍历字典 判断value是否是字符串  True就 re.findall 查找关键字替换

    :param case: 传入字典case
    :return: 替换后字典case
    """
    for key, value in case.items():
        if value is not None and isinstance(value, str):
            new_value = __replace_data(value)
            case[key] = new_value
    return case


def __replace_data(data: str):
    res = re.findall('#(.*?)#', data)
    if res:
        for mark_data in res:
            try:
                value = getattr(GlobalVar, mark_data)
            except:
                try:
                    value = cf.get_str('', str(mark_data))
                except:
                    continue
            data = data.replace("#{}#".format(mark_data), value)
    return data


if __name__ == '__main__':
    setattr(GlobalVar, 'email', 'shiyong@tetx.com')
    setattr(GlobalVar, 'goods', '10002163')
    str1 = {'test': 'dafgsassff(#email#)ad""(#goods#)sdasd'}
    print(replace_all_data(str1))

    aa = {
        "code": 0,
        "error": "",
        "msg": "success",
        "data": {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhemF6aWUiLCJhdWQiOiJ1c2VycyIsImlhdCI6MTY1OTE2NTIzNywiZXhwIjoxNjU5NzcwMDM3LCJ1c2VyX2lkIjo1ODYzMTc2fQ.eATIsczxh6LsKDDPWxGPaejDNm_8Ym2HtR-zMwtFkHE",
            "user_id": 5863176,
            "email": "aaacdhc12aaaw1a@tetx.com",
            "name": "aaacdhc12aaaw1a",
            "cartNumChanged": False,
            "isPreviewUser": False
        }
    }

    get_res_data(aa, '{"already_exist_email": "$..email"}')
