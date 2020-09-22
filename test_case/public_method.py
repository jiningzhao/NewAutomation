from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


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
