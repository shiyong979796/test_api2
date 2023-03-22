import pytest
from register import register
from common.handle_data import GlobalVar


@pytest.fixture(scope='class')
def cart_login():
    # user = register()
    # setattr(GlobalVar, 'token', user['data']['token'])
    datas = {'code': 0, 'error': '', 'msg': 'success', 'data': {
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhemF6aWUiLCJhdWQiOiJ1c2VycyIsImlhdCI6MTY2MTYwNjkxNiwiZXhwIjoxNjYyMjExNzE2LCJ1c2VyX2lkIjo2MTEyMTU5fQ.wCxwTcwFjaPrswWxrMcYAaSY2IW0W2KupI6Rw940oak',
        'user_id': 6112159, 'email': 'outotest20220827212836@tetx.com', 'name': 'outotest20220827212836',
        'cartNumChanged': False, 'isPreviewUser': False, 'isRetailer': False}}
    setattr(GlobalVar, 'token', datas['data']['token'])
    yield datas
    # yield None


if __name__ == '__main__':
    pass
