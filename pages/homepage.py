class HomePage:

    def __init__(self,driver):
        self.driver = driver
        self.logout_btb_id = "logoutLink"

    def logout(self):
        self.driver.find_element_by_id(self.logout_btb_id).click()