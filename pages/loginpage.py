from utils.constants import *
class LoginPage:

    def __init__(self,driver):
        self.driver=driver
        self.un_txt_bx_id= 'username'
        self.pwd_txt_bx_xpath="//input [@name ='pwd']"
        self.login_btb_xpath="//div[text()='Login ']"

    def enter_user_name(self):
        self.driver.find_element_by_id(self.un_txt_bx_id).send_keys(USER_NAME)

    def enter_password(self):
        self.driver.find_element_by_xpath(self.pwd_txt_bx_xpath).send_keys(PASSWORD)

    def click_on_login_btn(self):
        self.driver.find_element_by_xpath(self.login_btb_xpath).click()