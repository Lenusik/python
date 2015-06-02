__author__ = 'Lenusik'

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        # init group creation
        driver.find_element_by_name("new").click()

        #---HACK----
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(self.app.username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(self.app.password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_name("new").click()
        #-----

        # fill group form
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_group_page()

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()