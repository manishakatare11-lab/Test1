import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.Join_interview import join_interview


class Test_join_interview:

    def chrome_options(self):

        options = Options()

        options.add_argument("--incognito")

        options.add_argument("--use-fake-ui-for-media-stream")

        options.add_experimental_option(
            "prefs",
            {
                "profile.default_content_setting_values.media_stream_mic": 1,
                "profile.default_content_setting_values.media_stream_camera": 1,
                "profile.default_content_setting_values.notifications": 1,
                "profile.default_content_setting_values.geolocation": 1,
            },
        )

        return options

    def test_join_interview(self):

        driver = webdriver.Chrome(options=self.chrome_options())

        candidate = join_interview(driver)

        candidate.fill_candidate()
        candidate.allow_consent()
        #time.sleep(3)


        driver = webdriver.Chrome(options=self.chrome_options())

        interviewer = join_interview(driver)

        interviewer.interviewer_join(
            username="priya.Sharma@yopmail.com",
            password="VZ6n@tTStuHnBZV"
        )