import logging

from Pages.Login_Admin_page import Login_Admin_page
from selenium.webdriver.common.by import By

from utilities.read_properties import Read_Config
from utilities.customer_logger import Log_Maker


class Test_01_Admin_login:

    def setup_method(self):
        self.admin_page_url = Read_Config.get_admin_page_url()
        self.username = Read_Config.get_username()
        self.password = Read_Config.get_password()
        self.invalid_password = Read_Config.get_invalid_login()
        self.logger = Log_Maker.log_gen()


    def test_valid_admin_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        login = Login_Admin_page(self.driver)
        login.wait_for_page_load()
        login.accept_cookies()
        login.login(self.username, self.password)
        assert login.get_dashboard_text() == "TalentCentral+"
        logging.info("Logged in Successfully")
        self.driver.save_screenshot("..//Screenshots//screenshot1.png")

    def test_invalid_admin_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        login = Login_Admin_page(self.driver)
        login.accept_cookies()
        login.login(self.username, self.invalid_password)
        assert login.get_error_text() == "Your password is invalid!"
        logging.info("invalid login cred")