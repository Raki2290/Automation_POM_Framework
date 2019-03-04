import os
import pytest
from utils.constants import *

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in Your Browser Name e.g chrome, Firefox")
path= os.getcwd().replace("test","").replace("//","/")+ "Drivers/chromedriver.exe"
@pytest.fixture(scope= 'class')
def test_launch_browser(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path = "C:/Users/Indium Software/PycharmProjects/Automation_POM_Framework/Drivers/chromedriver.exe")
    elif browser == "Firefox":
        driver = webdriver.Firefox(executable_path= "C:/Users/Indium Software/PycharmProjects/Automation_POM_Framework/Drivers/geckodriver.exe")

    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(URL)
    request.cls.driver = driver

    yield
    driver.quit()
