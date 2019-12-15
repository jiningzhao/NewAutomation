import pytest
# import random
import json
from faker import Faker
from common.Assert import Assert
# from ..DB_fixture.mysql_db import DB_fixture
from params.tools import DisposeData


@pytest.fixture(scope='class')
def get_code():

    information = {
        'name': 'passport.login.security',
        'data': {
            "account": "18888888888",
            "password": "a111111",
            "returnUrl": "",
            "captcha": ""
        },
        'api': "/passport/api",
        'method': 'post'
    }
    result = DisposeData(information).response_()
    return result.get('value').split('=')[1]


@pytest.fixture(scope='class')
def get_token(get_code):
    information = {
        'name': 'passport.userinfo.bycode',
        'data': {
            "code": get_code
        },
        'api': "/passport/api",
        'method': 'post'
    }
    result = DisposeData(information).response_()
    return result.get('value').get('token')


@pytest.fixture(scope='class')
def random_massage():

    f = Faker(locale="zh_CN")
    massage = {
        'name': f.name()+"(JN)",
        'mobile': f.phone_number(),
        'ID_card': f.ssn(),
        'sentence': f.sentence(),
        'number(1-3)': f.random_int(min=1, max=3),
        'number(1-2)': f.random_int(min=1, max=2),
        'job': f.job()
    }

    return massage
