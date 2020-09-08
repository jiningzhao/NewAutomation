# coding=utf-8
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pytest


class TestCreateNewPlm:

    @pytest.mark.smoke
    # 新增收益管理方案
    def test_0(self, chrome_config):
        driver = chrome_config['driver']
        self.wait_element_clickable(driver, png_name="收益管理方案等待新增", xpath_str="//span[contains(text(),'新增方案')]")
        # 点击新增方案入口
        driver.execute_script("arguments[0].click()", driver.find_element_by_xpath("//span[contains(text(),'新增方案')]"))
        # 点击新增收益管理方案
        driver.execute_script("arguments[0].click()", driver.find_element_by_xpath("//li[contains(text(),'收益管理方案')]"))
        self.wait_element_clickable(driver, png_name="收益管理方案", classname='el-input__inner')

        # 输入方案名称
        driver.find_element_by_xpath("//input[@placeholder='输入方案名称']").send_keys(chrome_config['repayment_name'])
        # 选择回款方式
        driver.find_element_by_xpath("//input[@placeholder='请选择回款方式']").click()
        driver.execute_script("arguments[0].click()",
                              driver.find_element_by_xpath("//span[contains(text(),'一次性还本付息')]"))
        # 选择起息方式
        driver.find_element_by_xpath("//input[@placeholder='请选择起息方式']").click()
        driver.execute_script("arguments[0].click()",
                              driver.find_element_by_xpath("//span[contains(text(),'指定日起息')]"))

        # 选择期限类型
        driver.find_element_by_xpath("//input[@placeholder='请选择期限类型']").click()
        driver.execute_script("arguments[0].click()",
                              driver.find_element_by_xpath("//span[contains(text(),'指定到期日')]"))
        # 点击保存
        driver.execute_script("arguments[0].click()", driver.find_element_by_xpath("//section[contains(text(),'保存')]"))
        # 等待列表
        # self.wait_element_clickable(driver, png_name="等待列表加载", classname='el-table__row')
        # # 点击收益管理方案tab
        # driver.find_element_by_xpath("//div[contains(text(),'收益管理方案')]").click()
        # self.wait_element_clickable(driver,png_name="",classname='el-table__row')
        # self.name_assert(driver, chrome_config['repayment_name'])
        # time.sleep(10)

    @pytest.mark.smoke
    # 新增计算参数方案
    def test_1(self, chrome_config):
        driver = chrome_config['driver']
        self.wait_element_clickable(driver, png_name="计算参数方案等待新增", classname='el-menu-item')
        # 点击新增方案入口
        driver.execute_script("arguments[0].click()", driver.find_element_by_xpath("//span[contains(text(),'新增方案')]"))
        # 点击新增计算参数方案
        driver.execute_script("arguments[0].click()", driver.find_element_by_xpath("//li[contains(text(),'计算参数方案')]"))
        self.wait_element_clickable(driver, png_name="计算参数方案", classname='el-input__inner')
        # 输入方案名称
        driver.find_element_by_xpath("//input[@placeholder='输入方案名称']").send_keys(chrome_config['calculate_rule_name'])
        # 选择计算计息天数
        driver.find_element_by_xpath('//*[@id="pane-1"]/section/form/div[2]/div/div/div[2]/div/div[1]/input').click()
        driver.execute_script("arguments[0].click()",
                              driver.find_element_by_xpath("//span[contains(text(),'ACT/365')]"))
        # 选择小数舍入模式
        driver.find_element_by_xpath('//*[@id="pane-1"]/section/form/div[3]/div/div/div[2]/div/div[1]/input').click()
        driver.execute_script("arguments[0].click()",
                              driver.find_element_by_xpath("//span[contains(text(),'向下取整')]"))
        # 点击保存
        driver.execute_script("arguments[0].click()", driver.find_element_by_xpath("//section[contains(text(),'保存')]"))
        # driver.execute_script("arguments[0].click()", driver.find_element_by_xpath("//section[contains(text(),'返回')]"))
        # 等待列表刷新
        # self.wait_element_clickable(driver, png_name="等待列表加载", classname='el-table__row')
        # 点击计算参数方案tab
        # driver.find_element_by_xpath("//div[contains(text(),'计算参数方案')]").click()
        # self.wait_element_clickable(driver, 'el-table__row')
        # self.name_assert(driver, name=chrome_config['calculate_rule_name'])

    @pytest.mark.smoke
    # 新增额度管理方案
    def test_2(self, chrome_config):
        driver = chrome_config['driver']
        self.wait_element_clickable(driver, png_name="额度管理方案等待新增", classname='el-menu-item')
        # 点击新增方案入口
        driver.execute_script("arguments[0].click()",
                              driver.find_element_by_xpath("//span[contains(text(),'新增方案')]"))
        # 点击新增额度管理方案
        driver.execute_script("arguments[0].click()",
                              driver.find_element_by_xpath("//li[contains(text(),'额度管理方案')]"))
        self.wait_element_clickable(driver, png_name="额度管理方案", classname='el-input__inner')

        # 输入方案名称
        driver.find_element_by_xpath("//input[@placeholder='输入方案名称']").send_keys(chrome_config['limit_name'])

        # 点击保存
        driver.execute_script("arguments[0].click()",
                              driver.find_element_by_xpath("//section[contains(text(),'保存')]"))

        # self.wait_element_clickable(driver, 'el-table__row')
        # 点击额度管理方案tab
        # driver.find_element_by_xpath("//div[contains(text(),'额度管理方案')]").click()
        # self.wait_element_clickable(driver, 'el-table__row')
        # self.name_assert(driver, name=chrome_config['limit_name'])

    @pytest.mark.smoke
    # 新增贴息管理方案
    def test_3(self, chrome_config):
        driver = chrome_config['driver']
        self.wait_element_clickable(driver, png_name="贴息管理方案等待新增" 'el-menu-item')
        # 点击新增方案入口
        driver.execute_script("arguments[0].click()",
                              driver.find_element_by_xpath("//span[contains(text(),'新增方案')]"))
        # 点击新增贴息管理方案
        # self.wait_element(driver, xpath_str="//li[contains(text(),'贴息管理方案')]")
        driver.execute_script("arguments[0].click()",
                              driver.find_element_by_xpath("//li[contains(text(),'贴息管理方案')]"))
        # 输入方案名称
        self.wait_element_clickable(driver, png_name="贴息管理方案-输入方案名称", xpath_str="//input[@placeholder='输入方案名称']")

        driver.find_element_by_xpath("//input[@placeholder='输入方案名称']").send_keys(
            chrome_config['interest_allowance_name'])

        # 选择贴息起息方式
        self.wait_element_clickable(driver, png_name="贴息管理方案-选择起息方式", xpath_str="//input[@placeholder='请选择']")
        driver.find_elements_by_xpath("//input[@placeholder='请选择']")[0].click()

        self.wait_element_clickable(driver, png_name="贴息管理方案-选择指定起息日", xpath_str="//span[contains(text(),'指定起息日')]")

        driver.find_element_by_xpath("//li/span[contains(text(),'指定起息日')]").click()

        # 输入贴息到期日
        self.wait_element_clickable(driver, png_name="贴息管理方案-选择贴息到期日", xpath_str="//input[@placeholder='请选择']")
        driver.find_elements_by_xpath("//input[@placeholder='请选择']")[1].click()
        self.wait_element_clickable(driver, png_name="贴息管理方案-选择指定到期日", xpath_str="//span[contains(text(),'指定到期日')]")
        driver.find_element_by_xpath("//li/span[contains(text(),'指定到期日')]").click()

        # 清除readonly属性
        self.wait_element_clickable(driver, png_name="贴息管理方案-选择贴息发放时间", xpath_str="//input[@placeholder='请选择']")

        # 输入贴息发放时间
        driver.find_elements_by_xpath("//input[@placeholder='请选择']")[2].click()
        self.wait_element_clickable(driver, png_name="贴息管理方案-选择指定日发放", xpath_str="//span[contains(text(),'指定日发放')]")
        driver.find_element_by_xpath("//li/span[contains(text(),'指定日发放')]").click()

        self.wait_element_clickable(driver, png_name="贴息管理方案-保存", xpath_str="//section[contains(text(),'保存')]")
        # 点击保存
        driver.find_element_by_xpath("//section[contains(text(),'保存')]").click()
        # self.wait_element_clickable(driver, 'el-table__row')
        # # 点击贴息管理方案tab
        # driver.find_element_by_xpath("//div[contains(text(),'贴息管理方案')]").click()
        # self.wait_element_clickable(driver, 'el-table__row')
        # self.name_assert(driver, name=chrome_config['interest_allowance_name'])

    @staticmethod
    def wait_element_clickable(driver, png_name, classname=None, xpath_str=None):
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
                wait.until(EC.element_to_be_clickable((By.CLASS_NAME, classname)),
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

    @staticmethod
    def name_assert(driver, name):
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_any_elements_located((By.XPATH, '//p[contains(text(),"操作成功")]')),
                message="定位【操作成功】文案失败！")
        except Exception as e:
            driver.get_screenshot_as_file(
                '../dir_screenshot/{}.png'.format(
                    name + "{}".format(e)))
            assert 1 != 1, e
        finally:
            pass
