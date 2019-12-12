# -*- coding:utf-8 -*-
# import pytest
# from ..params.param_template import json_template
# from ..common.api import ApiCall
# from ..params.tools import GetYaml
# from ..common.Assert import Assert
# import pytest
from params.tools import GetYaml
from common.Assert import Assert


class TestAddMarketProcess:

    @staticmethod
    def one_test(get_token):

        name = 'obj.pageinfo.get'

        response = GetYaml('add_market_test', headers=get_token).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])

    @staticmethod
    def two_test(get_token):

        name = 'obj.pageinfo.get'

        response = GetYaml('add_market_test', headers=get_token).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])

    @staticmethod
    def three_test(get_token):

        name = 'obj.objfield.selectshowjson'

        response = GetYaml('add_market_test', headers=get_token).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])

    @staticmethod
    def four_test(get_token):

        name = 'ac.activityType.list2'

        response = GetYaml('add_market_test', headers=get_token).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])

    @staticmethod
    def five_test(get_token):

        name = 'ac.labelConf.list2'

        response = GetYaml('add_market_test', headers=get_token).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])

    @staticmethod
    def add_market_test(get_token, random_massage):

        name = 'ac.activity.add'
        other_data = {'name': random_massage['sentence']+'(JN)'}
        response = GetYaml('add_market_test', other_data=other_data, headers=get_token).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])
