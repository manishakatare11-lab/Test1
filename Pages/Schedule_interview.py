import random
import string
import time
import pyperclip
from base_page.base_page import BasePage

class ScheduleInterview(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver,"Locators/Schedule_Interview/Schedule_Interview.json")

    def add_details(self, dropdown_name, index):
        self.do_select_DD(dropdown_name, index)
        #time.sleep(5)
        print("select igb")

    def add_interviewer(self):
        # Random text generate
        random_text = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

        #dynamic value
        candidate_name= f"test_{random_text}"
        candidate_email = f"test_{random_text}@yopmail.com"


        locator = self.locators.get("Interviewer")

        self.scroll_down_until_element(locator)

        self.do_click("Interviewer")
        self.do_send_keys("SearchInterviewer", "priya")
        time.sleep(5)
        self.do_click("Checkbox")
        self.do_click("Interviewer")
        self.do_send_keys("CandidateName", candidate_name)
        self.do_send_keys("CandidateEmail", candidate_email)
        locator1 = self.locators.get("ScheduleButton")
        self.scroll_down_until_element(locator1)
        self.do_click("ScheduleButton")
        try:
           if self.is_element_visible("ScheduleanywayButton", timeout=5):
               self.do_click("ScheduleanywayButton")
               print("ScheduleanywayButton is clicked")
           elif self.is_element_visible("Inviteinterviewers", timeout=5):
               print("Common login url is clicked")
           else:
               raise Exception("Common login url not found")

        except Exception:
            print("scheduling validation failed ")
        time.sleep(20)

        self.do_click("commonlogin")
        time.sleep(2)
        common_login_url = pyperclip.paste()

        print(common_login_url)
        self.Save_details(candidate_name, candidate_email, common_login_url)
        print("interview scheduled")








