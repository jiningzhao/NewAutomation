# import pytest
# from ..params.param_template import json_template
# from ..common.api import ApiCall
# from ..params.tools import GetYaml
# from ..common.Assert import Assert
import pytest
from params.tools import GetYaml
from common.Assert import Assert


class TestAddEmployeeProcess:

    @pytest.fixture()
    def test_add_department(self, get_token, random_massage):

        # 传入接口名称
        name = 'old_add_department'

        # 参数化
        other_data = {
                'name': str(random_massage['job']).replace("/",  ""),
                'departmentTypeCode': random_massage['number(1-2)']
        }
        # 调用函数并取出返回值
        response = GetYaml('add_employee', other_data=other_data, headers=get_token).case_select(name)

        # 从返回值中取数据并进行断言
        Assert(response['assert_type'], response['result']['success'], response['check'], response['result'])

        # 返回想要的数据
        return response['result']['data']

    @pytest.fixture()
    def test_add_position(self, get_token, random_massage):

        name = 'old_add_position'
        other_data = {
                'name': random_massage['job'],
                'propertyCode': random_massage['number(1-3)']
        }

        response = GetYaml('add_employee', other_data=other_data, headers=get_token).case_select(name)

        Assert(response['assert_type'], response['result']['success'], response['check'], response['result']['msg'])

        return response['result']['data']

    def test_add_employee(self, get_token, random_massage, test_add_position, test_add_department):

        name = 'passport.employee.add'

        other_data = {
            'mobile': random_massage['mobile'],
            'name': random_massage['name'],
            'documentNo': random_massage['ID_card'],
            'positionId': test_add_position,
            'deptIds': [test_add_department]
        }

        response = GetYaml('add_employee', other_data=other_data, headers=get_token).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])

        # Assert('IN', other_data['mobile'], 'mobile', None, response['DB_table'])


if __name__ == '__main__':
    # pytest.main(['-v','-s','--setup-show'])
    # pytest.main(['-v','--pdb'])
    pytest.main(['-v', '-s', 'add_product_test.py'])
    # pytest.main(['--collect-only'])
    # pytest.main(['--html=../report/report3.html'])
