import logging
import random
import string
import time

from Pages.Schedule_interview import ScheduleInterview
from Pages.interview import Contact
from Test_cases.conftest import setup


class Test_Schedule_Interview:

    def test_schedule_interview(self,  login_setup):
        logging.info("Test Schedule_Interview")
        driver =  login_setup

        contact = Contact(driver)
        contact.click_interview()
        contact.wait_for_page_load()

        schedule = ScheduleInterview(driver)
        schedule.add_details("IGB", 2)
        time.sleep(5)
        #random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

        #title = f"Interview_{random_text}"
        #schedule.add_title(title)
        schedule.add_interviewer()



