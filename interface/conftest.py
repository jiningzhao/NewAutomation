import pytest
# import random
from faker import Faker
from params.tools import GetYaml
from common.Assert import Assert
# from ..DB_fixture.mysql_db import DB_fixture


@pytest.fixture(scope='class')
def get_code():

    name = 'passport.login.security'

    response = GetYaml('login').case_select(name)

    code = str(response['result']['value']).split('code=')[-1]

    Assert(response['assert_type'], code, response['check'], response['detail'])

    return code


@pytest.fixture(scope='class')
def get_token(get_code):

    name = 'passport.userinfo.bycode'

    other_data = {'code': get_code}

    response = GetYaml('login', other_data=other_data).case_select(name)

    token = response['result']['value']['token']

    Assert(response['assert_type'], token, response['check'], response['detail'])

    return token


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
