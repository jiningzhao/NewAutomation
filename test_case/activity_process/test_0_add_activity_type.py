# coding=utf-8
import pytest
from ...common.tools import DisposeData
from ...config.config import Conf


class TestAddNewActivityType:
    # @pytest.mark.smoke
    @pytest.mark.smoke0
    def test_add_new_activity_type(self, get_token, random_massage):
        information = {
            'name': 'ac.activityType.add',
            'data': {
                "typeName": random_massage.get('activity_type'),
                "sortNum": "1",
                "showStatus": 2,
                "entId": Conf().api_conf().get('entId'),
                "labelName": ""
            },
            'api': '/ac-web/api',
            'method': 'post'
        }

        DisposeData(information, get_token).response_()
