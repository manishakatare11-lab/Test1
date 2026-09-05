import time
import openpyxl

from Pages.Login_Admin_page import Login_Admin_page
from base_page.base_page import BasePage


class join_interview(BasePage):

    # Class Variable (shared)
    common_login_url = None

    def __init__(self, driver):
        self.driver = driver
        self.interviewlogin = Login_Admin_page(driver)

        super().__init__(driver, "Locators/Join_Interview/Join_Interview.json")

    def fill_candidate(self):

        candidate_data = self.read_excel()

        for candidate_name, candidate_email, common_login_url in candidate_data:

            # Save URL
            join_interview.common_login_url = common_login_url

            self.driver.get(common_login_url)

            self.wait_for_page_load()
            self.accept_cookies()

            self.do_send_keys("CandidateName", candidate_name)
            self.do_send_keys("CandidateEmail", candidate_email)

            self.do_click("Join")

            time.sleep(5)

    def allow_consent(self):
        self.driver.maximize_window()
        self.do_click("aiSummaryConsentcheckbox")
        self.do_click("recordConsentcheckbox")
        self.do_click("dpnConsentCheckbox")
        self.do_click("JoinCandidate")

        time.sleep(10)



    def interviewer_join(self, username, password):

        print(join_interview.common_login_url)

        self.driver.get(join_interview.common_login_url)

        self.wait_for_page_load()
        self.accept_cookies()
        self.driver.maximize_window()

        self.do_click("JoinAsInterviewer")

        self.interviewlogin.login(username, password)

        self.do_click("JoinInterview")