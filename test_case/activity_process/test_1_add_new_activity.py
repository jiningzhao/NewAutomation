# coding=utf-8
import time
import pytest
from ...config.config import Conf
from ...common.tools import DisposeData
from ..public_method import wait_element_visibility
from ..public_method import wait_element_clickable
import json


class TestAddNewActivity:

    # @pytest.mark.smoke
    @pytest.fixture(scope='session')
    # 登陆
    def ui_token(self, chrome_config):
        driver = chrome_config['driver']
        driver.maximize_window()
        driver.get(Conf().api_conf().get('url'))
        # 等待元素出现
        wait_element_clickable(driver, png_name="登录异常", xpath_str='//input')
        # 定位用户名输入框并输入手机号
        elem = driver.find_element_by_xpath(
            "/html/body/section/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div/div/div/input")
        elem.clear()
        elem.send_keys("18888888888")
        # 定位密码输入框并输入密码
        elem = driver.find_element_by_xpath(
            "/html/body/section/div[1]/div/div[2]/div/div/div[2]/form/div[2]/div/div/div[1]/input")
        elem.clear()
        elem.send_keys("a111111")
        # 定位登录按钮并点击
        driver.find_element_by_xpath("//span[contains(text(),'登录')]").click()
        # 等待元素出现
        wait_element_clickable(driver, png_name="首页加载异常", classname='el-menu-item')
        token = driver.execute_script('return localStorage.getItem("access_token");')
        print(json.loads(token).get('a'))
        return json.loads(token).get('a')

    @pytest.mark.smoke
    # 点击进入市场活动页面
    def test_1(self, chrome_config, ui_token):
        driver = chrome_config['driver']
        time.sleep(5)
        driver.execute_script("arguments[0].click()",
                              driver.find_element_by_xpath("//li/span[contains(text(),'市场活动')]"))
        wait_element_clickable(driver, png_name="新增市场活动按钮未找到", xpath_str="//div[contains(text(),'新增市场活动')]")
        driver.execute_script("arguments[0].click()", driver.find_element_by_xpath("//div[contains(text(),'新增市场活动')]"))
        wait_element_visibility(driver, png_name="新增市场活动页", xpath_str="//div[contains(text(),'基本信息')]")
        driver.find_element_by_xpath("//section[contains(text(),'返回')]").click()

    @pytest.mark.smoke
    # 通过接口新增市场活动
    def test_2(self, ui_token, random_massage):
        information = {
            'name': 'ac.activity.add',
            'data': {
                "name": "活动" + str(random_massage.get("uuid")),
                "startTime": "2020-09-01 15:56:33",
                "endTime": "2020-09-30 15:56:38",
                "scope": {
                    "innerAdvisorScope": {
                        "officeIds": [],
                        "deptCodes": [],
                        "labelIds": [],
                        "type": -1
                    },
                    "outsideAdvisorScope": {
                        "type": -1
                    },
                    "customerScope": {
                        "labelIds": [-1],
                        "type": -1
                    }
                },
                "shareCfg": 1,
                "shareChannel": [1, 2],
                "signUpResult": 1,
                "pictureUrl": "https://pic.newbanker.cn/img/2066/2020/9/17/50162092099545dbb784827085cf8ff5.png",
                "evaluationPeriod": 30,
                "typeId": 5,
                "summary": "活动简介",
                "deptCode": {
                    "id": 1,
                    "code": "GTEAMM0001",
                    "parentCode": "",
                    "name": "总裁办",
                    "empCnt": 0,
                    "departmentTypeCode": 1,
                    "childs": []
                }
            },
            'api': '/ac-web/api',
            'method': 'post'
        }
        DisposeData(information, ui_token).response_()

    @pytest.mark.smoke
    # 刷新页面并点击未发布tab
    def test_3(self, chrome_config, random_massage):
        driver = chrome_config['driver']
        driver.refresh()
        wait_element_clickable(driver, png_name="刷新市场活动页面", xpath_str="//div[contains(text(),'未发布')]")
        driver.find_element_by_xpath("//div[contains(text(),'未发布')]").click()
        wait_element_clickable(driver, png_name="验证市场活动添加成功",
                               xpath_str="//a[contains(text(),\'{}\')]".format("活动" + str(random_massage.get("uuid"))))

    @pytest.fixture()
    def activity_no(self, chrome_config, random_massage):
        driver = chrome_config['driver']
        driver.find_element_by_xpath(
            "//a[contains(text(),\'{}\')]".format("活动" + str(random_massage.get("uuid")))).click()
        wait_element_clickable(driver, png_name="活动编号",
                               xpath_str="//div/div[contains(text(),'活动编号')]/following-sibling::*/span")
        return driver.find_element_by_xpath("//div/div[contains(text(),'活动编号')]/following-sibling::*/span").text

    @pytest.mark.smoke
    def test_4(self, activity_no, test_0):
        information = {
            'name': 'ac.activity.add.timingdate',
            'data': {
                "timingDate": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
                "no": activity_no
            },
            'api': '/ac-web/api',
            'method': 'post'
        }
        DisposeData(information, test_0).response_()

    @pytest.mark.smoke
    def test_5(self, chrome_config):
        driver = chrome_config['driver']
        driver.find_element_by_xpath("//button/span[contains(text(),'编辑')]").click()
        time.sleep(3)
        wait_element_clickable(driver, png_name="活动编辑页", xpath_str="//div[contains(text(),'基本信息')]")
        driver.find_element_by_xpath("//span[contains(text(),'返回')]").click()
        wait_element_clickable(driver, png_name="返回列表", xpath_str="//section[contains(text(),'返回')]")
        driver.find_element_by_xpath("//section[contains(text(),'返回')]").click()
        time.sleep(3)

    @pytest.mark.smoke
    def test_5(self, ui_token, random_massage):
        information = {
            'name': 'fs.auth.upload.access.upload.token',
            'data': {
                "isPubRead": 1,
                "filename": "1587695841112140.mp4"
            },
            'api': 'fs-upload',
            'method': 'post'
        }

        DisposeData(information, ui_token).response_()
