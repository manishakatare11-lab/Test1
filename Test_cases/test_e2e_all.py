from Test_cases.test_schedule_interview import Test_Schedule_Interview
from Test_cases.test_join_interview import Test_join_interview



class TestE2EFlow():
   def test_e2e_schedule_and_join(self, login_setup):
        """
        Full E2E: schedule interview as admin, then join as candidate and interviewer.
        Re-uses existing page objects/helpers. Cleans up browser instances it creates.
        """
        # 1) Schedule interview using the logged-in admin session (login_setup fixture)
        admin_driver = login_setup
        contact = Contact(admin_driver)
        contact.click_interview()
        contact.wait_for_page_load()

        schedule = ScheduleInterview(admin_driver)
        # choose dropdown "IGB" and option index 2 as in original test
        schedule.add_details("IGB", 2)
        # add interviewer which will also generate candidate details and call Save_details(...)
        schedule.add_interviewer()

        # Give file write a moment (Save_details writes details.xlsx). In practice the ScheduleInterview
        # implementation already sleeps; this is an additional safeguard.
        time.sleep(2)

        # 2) Candidate: open a fresh browser and use join_interview.fill_candidate() to read the saved details.xlsx
        candidate_driver = webdriver.Chrome(options=_chrome_options_with_fake_media())
        # Ensure candidate driver is closed later
        interviewer_driver = None

        try:
            candidate = join_interview(candidate_driver)
            candidate.fill_candidate()
            candidate.allow_consent()

            # After fill_candidate, the join_interview.common_login_url class variable should be set
            common_url = join_interview.common_login_url
            assert common_url is not None and common_url.startswith("http"), "Common login URL not written/read correctly"

            # 3) Interviewer: open another fresh browser and join using interviewer credentials
            interviewer_driver = webdriver.Chrome(options=_chrome_options_with_fake_media())
            interviewer = join_interview(interviewer_driver)
            interviewer.interviewer_join(
                username=INTERVIEWER_USERNAME,
                password=INTERVIEWER_PASSWORD
            )

            # Small wait to allow the interviewer join action to proceed
            time.sleep(5)

            # Basic verification: the common url used by join flow should still be present
            assert join_interview.common_login_url == common_url

        finally:
            # Cleanup created browser instances so tests do not leak resources
            try:
                candidate_driver.quit()
            except Exception:
                pass
            if interviewer_driver:
                try:
                    interviewer_driver.quit()
                except Exception:
                    pass
