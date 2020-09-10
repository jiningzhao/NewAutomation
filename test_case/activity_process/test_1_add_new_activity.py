# coding=utf-8
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from ...config.config import Conf


class TestPlmMenu:

    @pytest.mark.smoke
    # 登陆
    def test_0(self, chrome_config):
        driver = chrome_config['driver']
        driver.maximize_window()
        driver.get(Conf().api_conf().get('url'))
        # 等待元素出现
        self.wait_element(driver, png_name="登录异常", xpath_str='//input')
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
        self.wait_element(driver, png_name="首页加载异常", classname='el-menu-item')

    @pytest.mark.smoke
    # 点击进入市场活动页面
    def test_1(self, chrome_config):
        driver = chrome_config['driver']
        time.sleep(5)
        driver.execute_script("arguments[0].click()", driver.find_element_by_xpath("//span[contains(text(),'市场活动')]"))
        self.wait_element(driver, png_name="新增市场活动按钮未找到", xpath_str="//div[contains(text(),'新增市场活动')]")
        driver.execute_script("arguments[0].click()", driver.find_element_by_xpath("//div[contains(text(),'新增市场活动')]"))
        self.wait_element_visibility(driver, png_name="新增市场活动页", xpath_str="//div[contains(text(),'基本信息')]")
        driver.find_element_by_xpath("//input[@placeholder='最多30个字']").send_keys("自动化测试")

        driver.execute_script('arguments[0].removeAttribute("readonly")',
                              driver.find_elements_by_xpath("//input[@placeholder='请选择时间']")[0])
        driver.find_elements_by_xpath("//input[@placeholder='请选择时间']")[0].send_keys('2020-09-09 18:00:21')

        driver.execute_script('arguments[0].removeAttribute("readonly")',
                              driver.find_elements_by_xpath("//input[@placeholder='请选择时间']")[1])
        driver.find_elements_by_xpath("//input[@placeholder='请选择时间']")[1].send_keys('2020-10-10 18:00:21')
        ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="pane-0"]/div')).click().perform()
        time.sleep(2)
        driver.find_element_by_name('file').send_keys('../img/活动海报.png')
        time.sleep(10)

    @staticmethod
    def wait_element(driver, png_name, classname=None, xpath_str=None):
        try:
            wait = WebDriverWait(driver, 10)
            if classname is not None:
                wait.until(EC.element_to_be_clickable((By.CLASS_NAME, classname)),
                           message="超时！/等待class元素:{}失败！".format(classname))
            elif xpath_str is not None:
                wait.until(EC.element_to_be_clickable((By.XPATH, xpath_str)),
                           message="超时！/等待xpath路径:{}失败！".format(xpath_str))
        except Exception as e:
            driver.get_screenshot_as_file(
                '../dir_screenshot/{}.png'.format(png_name))
            assert 1 != 1, e

        finally:
            pass

    @staticmethod
    def wait_element_visibility(driver, png_name, classname=None, xpath_str=None):
        try:
            wait = WebDriverWait(driver, 10)
            if classname is not None:
                wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, classname)),
                           message="超时！/等待class元素:{}失败！".format(classname))
            elif xpath_str is not None:
                wait.until(EC.visibility_of_any_elements_located((By.XPATH, xpath_str)),

                           message="超时！/等待xpath路径:{}失败！".format(xpath_str))
        except Exception as e:
            driver.get_screenshot_as_file(
                '../dir_screenshot/{}.png'.format(png_name))
            assert 1 != 1, e

        finally:
            pass
