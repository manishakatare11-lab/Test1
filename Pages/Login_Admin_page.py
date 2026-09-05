import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_page.base_page import BasePage


class Login_Admin_page(BasePage):

    def __init__(self, driver):
        super().__init__(driver, "Locators/Login_Admin_page/login_admin_page.json")




    def login(self, username, password):
        self.wait_for_page_load()
        self.accept_cookies()  # yaha add karo

        self.do_send_keys("Username", username)
        self.do_send_keys("Password", password)
        self.do_click("Submit")
        self.driver.save_screenshot("..//Screenshots//login_page1.png")
        print("Login method called")

    def get_dashboard_text(self):
        return self.get_text("act_dashboard_text")

    def invalid_login(self, username, invalid_password):
        self.do_send_keys("Username", username)
        self.do_send_keys("Password", invalid_password)
        self.do_click("Submit")
        self.driver.save_screenshot("..//Screenshots//login_page_failed.png")
        print("Login method failed")


    def get_error_text(self):
        return self.get_text("act_validation_text")




