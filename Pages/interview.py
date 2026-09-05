import logging

from base_page.base_page import BasePage

class Contact(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver,"Locators/Interview/Interview.json")


    def click_interview(self):
        self.do_click("Interviews")
        self.do_click("Configure_and_schedule")
        self.do_click("SIP")
        logging.info("Contact Link clicked")



    #def fill_form(self, FirstName, LastName, Email, Comment):
     #   self.do_send_keys("FirstName", "manisha")
      #  self.do_send_keys("LastName", "katare")
       # self.do_send_keys("Email", "pooja@yopmail.com")
        #self.do_send_keys("Comment", "Hi")
        #self.do_click("Submit")








