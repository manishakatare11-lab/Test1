from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.Join_interview import join_interview
from utilities.read_properties import Read_Config


class Test_join_interview:

    @staticmethod
    def chrome_options():
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--use-fake-ui-for-media-stream")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
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
        properties = Read_Config()
        username = properties.get_username()
        password = properties.get_password()

        candidate_driver = webdriver.Chrome(options=self.chrome_options())
        try:
            candidate = join_interview(candidate_driver)
            candidate.fill_candidate()
            candidate.allow_consent()
            candidate.join_candidate()
        finally:
            candidate_driver.quit()

        interviewer_driver = webdriver.Chrome(options=self.chrome_options())
        try:
            interviewer = join_interview(interviewer_driver)
            interviewer.interviewer_join(
                username=username,
                password=password,
            )
            interviewer.Enter_interview()
        finally:
            interviewer_driver.quit()
