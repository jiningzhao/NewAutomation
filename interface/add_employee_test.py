# import pytest
# from ..params.param_template import json_template
# from ..common.api import ApiCall
# from ..params.tools import GetYaml
# from ..common.Assert import Assert
import pytest
from params.tools import DisposeData
# from params.tools import GetYaml
from common.Assert import Assert


class TestAddEmployeeProcess:

    @pytest.fixture()
    def test_add_department(self, random_massage, get_token):
        # 接口名称为key,data为value
        information = {
            'name': "old_add_department",
            'param': {
                'name': str(random_massage['job']).replace("/",  ""),
                'departmentTypeCode': random_massage['number(1-2)']
            },
            'api': "/http/saas/department/addTopDept.json",
            'method': 'post'
        }
        result = DisposeData(information, get_token).response_()
        return result.get('data')

    @pytest.fixture()
    def test_add_position(self, get_token, random_massage):
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

    def test_add_employee(self, get_token, random_massage, test_add_position, test_add_department):

        information = {
            'name': 'passport.employee.add',
            'data': {
                'name': random_massage['name'],
                'email': '',
                'gender': 0,
                'mobile': random_massage['mobile'],
                'deptIds': [test_add_department],
                'married': '',
                'roleIds': [],
                'joinDate': '2019-11-27',
                'managers': [0],
                'education': 2,
                'documentNo': random_massage['ID_card'],
                'employeeNo': '',
                'positionId': test_add_position,
                'defaultDept': '',
                'documentType': 2
            },
            'api': '/passport/api',
            'method': 'post'

        }
        DisposeData(information, get_token).response_()


if __name__ == '__main__':
    # pytest.main(['-v','-s','--setup-show'])
    # pytest.main(['-v','--pdb'])
    pytest.main(['-v', '-s', "add_employee_test.py"])
    # pytest.main(['--collect-only'])
    # pytest.main(['--html=../report/report3.html'])
