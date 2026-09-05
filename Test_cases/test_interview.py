import time

from Pages.interview import Contact


class Test_Contact_Customer:

    def test_contact_page(self, login_setup):
        driver = login_setup
        contact = Contact(driver)
        contact.click_interview()
        contact.wait_for_page_load()
        time.sleep(5)
        print("click interview")

       # assert contact.get_name_text() == "Contact"

