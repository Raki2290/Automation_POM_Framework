import time
import os
import pytest
from selenium import webdriver
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from utils.constants import *

@pytest.mark.usefixtures("test_launch_browser")
class TestLogin:
    def test_login(self):
        driver=self.driver
        lp= LoginPage(driver)
        lp.enter_user_name()
        lp.enter_password()
        lp.click_on_login_btn()


        # driver.find_element_by_id("username").send_keys("admin")
        # driver.find_element_by_xpath("//input [@name ='pwd']").send_keys("manager")
        # driver.find_element_by_xpath("//div[text()='Login ']").click()

    def test_logout(self):
        driver=self.driver
        time.sleep(5)
        lo= HomePage(driver)
        lo.logout()
        # driver.find_element_by_id("logoutLink").click()
        # driver.close()
#
#
#
# # launch_browser()
# # login()
# # logout()