from Test_cases.test_schedule_interview import Test_Schedule_Interview as ScheduleFlow, Test_Schedule_Interview
from Test_cases.test_join_interview import Test_join_interview as JoinFlow, Test_join_interview

Test_Schedule_Interview.__test__ = False
Test_join_interview.__test__ = False
class TestE2EFlow:

    def test_schedule_interview(self, login_setup):
        schedule_test = ScheduleFlow()
        schedule_test.test_schedule_interview(login_setup)

    def test_join_interview(self):
        join_test = JoinFlow()
        join_test.test_join_interview()



