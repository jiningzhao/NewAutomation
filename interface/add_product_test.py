from params.tools import GetYaml
from common.Assert import Assert
import pytest


class TestAddProductProcess:

    @pytest.fixture(scope='class')
    def add_product_test(self, get_token, random_massage):

        name = 'pdc.product.add'
        other_data = {'name': random_massage['sentence']+'(JN)'}
        response = GetYaml('add_product', other_data=other_data, headers=get_token).case_select(name)

        Assert(response['assert_type'], response['result']['success'], response['check'], response['result']['msg'])
        print(other_data['name'])
        return response['result']['data']

    @staticmethod
    def edit_product_config_test(get_token, add_product_test):

        name = 'old.product.config'
        other_data = {'id': add_product_test}
        response = GetYaml('add_product', other_data=other_data, headers=get_token).case_select(name)

        Assert(response['assert_type'], response['result']['success'], response['check'], response['result']['msg'])

    @staticmethod
    def edit_product_commission_test(get_token, add_product_test):
        name = 'old.product.commission'
        other_data = {'productId': add_product_test}
        response = GetYaml('add_product', other_data=other_data, headers=get_token).case_select(name)

        Assert(response['assert_type'], response['result']['success'], response['check'], response['result']['msg'])

    @staticmethod
    def edit_product_performance_test(get_token, add_product_test):
        name = 'old.product.performance'
        other_data = {'productId': add_product_test}
        response = GetYaml('add_product', other_data=other_data, headers=get_token).case_select(name)

        Assert(response['assert_type'], response['result']['success'], response['check'], response['result']['msg'])
