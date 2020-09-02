# coding=utf-8
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.common.exceptions import NoSuchElementException
# from ..config.config import Conf
from config.config import Conf


class TestPlmMenu:

    @pytest.mark.smoke
    # 登陆并验证页面中存在运营中心菜单
    def test_0(self, chrome_config):
        driver = chrome_config['driver']
        driver.maximize_window()
        driver.get(Conf().api_conf().get('url'))
        # 等待元素出现
        self.wait_element(driver, classname='el-input__inner')
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
        self.wait_element(driver, classname='el-menu-item')
        # assert "运营中心" in self.driver.page_source, "msg=页面不存在运营中心文案"

    @pytest.mark.smoke
    # 跳转到运营中心页面
    def test_1(self, chrome_config):
        driver = chrome_config['driver']
        self.wait_element(driver, classname='el-menu-item')
        # 定位元素位置并使用js点击，点击"运营中心"按钮跳转到运营中心页面，如不存在运营中心按钮截图并断言失败
        try:
            button = driver.find_element_by_xpath("//span[text()='运营中心']")
        except NoSuchElementException as e:
            driver.get_screenshot_as_file(
                '../dir_screenshot/{}.png'.format("不存在运营中心菜单项" + time.strftime("%Y%m%d%H%M%S", time.localtime())))
            assert 1 != 1, e
        driver.execute_script("arguments[0].click()", button)
        driver.switch_to.window(driver.window_handles[-1])
        self.wait_element(driver, classname='el-menu-item')
        # driver.get_screenshot_as_file(
        #     '../dir_screenshot/{}.png'.format("测试" + time.strftime("%Y%m%d%H%M%S", time.localtime())))
        # self.assertIn("服务运营管理", driver.page_source, "msg=跳转到运营中心页面超时！")

    @pytest.mark.smoke
    # 跳转到运营方案管理页面
    def test_2(self, chrome_config):
        driver = chrome_config['driver']
        self.wait_element(driver, classname='el-menu-item')
        button = driver.find_element_by_xpath("//li[contains(text(),'运营方案管理')]")
        driver.execute_script("arguments[0].click()", button)

    @staticmethod
    def wait_element(driver, classname=None, xpath_str=None):
        try:
            wait = WebDriverWait(driver, 10)
            if classname is not None:
                wait.until(EC.element_to_be_clickable((By.CLASS_NAME, classname)),
                           message="超时！/等待class元素:{}失败！".format(classname))
            elif xpath_str is not None:
                # wait.until(EC.visibility_of_any_elements_located((By.XPATH, xpath_str)),
                wait.until(EC.element_to_be_clickable((By.XPATH, xpath_str)),
                           message="超时！/等待xpath路径:{}失败！".format(xpath_str))
        except Exception as e:
            driver.get_screenshot_as_file(
                '../dir_screenshot/{}.png'.format("xpath路径异常" + time.strftime("%Y%m%d%H%M%S", time.localtime())))
            assert 1 != 1, e

        finally:
            pass


if __name__ == "__main__":
    # pytest.main(['-v', '--tb=line', '-m=smoke', '--junitxml=test-report.xml'])
    pytest.main(['-v', '-s', '-m=smoke'])
