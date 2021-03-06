# coding=utf-8
import pytest
from faker import Faker
# from DB_fixture.mysql_db import DB_fixture
from ...common.tools import DisposeData
# from common.tools import DisposeData
from ...config.config import Conf
# from config.config import Conf
from selenium import webdriver
import uuid


@pytest.fixture(scope='session')
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


@pytest.fixture(scope='session')
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


@pytest.fixture(scope='session')
def random_massage(request):
    f = Faker(locale="zh_CN")
    massage = {
        'name': f.name() + "(JN)",
        'mobile': f.phone_number(),
        # 'mobile': request.param,
        'ID_card': f.ssn(),
        'sentence': f.sentence(),
        'number(1-3)': f.random_int(min=1, max=3),
        'number(1-2)': f.random_int(min=1, max=2),
        'number(300-400)': f.random_int(min=300, max=400),
        'number(1-400)': f.random_int(min=1, max=400),
        'uuid': uuid.uuid1(),
        # 'number': request.param,
        'job': f.job(),
        'activity_type': '活动类型'
    }

    return massage


@pytest.fixture(scope='session')
def test_add_department(random_massage, get_token):
    information = {
        'name': "old_add_department",
        'param': {
            'name': str(random_massage['job']).replace("/", ""),
            'departmentTypeCode': random_massage['number(1-2)']
        },
        'api': "/http/saas/department/addTopDept.json",
        'method': 'post'
    }
    result = DisposeData(information, get_token).response_()
    return result.get('data')


@pytest.fixture(scope='class')
def test_add_position(get_token, random_massage):
    information = {
        'name': 'old_add_position',
        'param': {
            'name': random_massage['job'],
            'propertyCode': random_massage['number(1-3)']
        },
        'api': "/http/saas/position/add.json",
        'method': 'post'
    }
    response = DisposeData(information, get_token).response_()
    return response.get('data')


@pytest.fixture(scope='session')
def chrome_config(random_massage):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('--incognito')
    chrome_option.add_argument('--blink-settings=imagesEnabled=false')
    chrome_option.add_experimental_option('useAutomationExtension', False)
    chrome_option.add_experimental_option("excludeSwitches", ['enable-automation'])
    details = {
        'driver': webdriver.Chrome(options=chrome_option)
    }
    return details
