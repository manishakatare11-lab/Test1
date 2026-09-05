from Test_cases.test_schedule_interview import Test_Schedule_Interview
from Test_cases.test_join_interview import Test_join_interview



class TestE2EFlow():
    def test_e2e(self, login_setup):
        schedule_test = Test_Schedule_Interview()
        join_interviewer = Test_join_interview()
        schedule_test.test_schedule_interview(login_setup)
        join_interviewer.test_join_interview()

    def test_checknew(self):
        join_interviewer = Test_join_interview()
        sys("test")