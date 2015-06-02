__author__ = 'Lenusik'
from selenium import webdriver

class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"

        self.username = "admin"
        self.password = "secret"

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def return_to_group_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def create_group(self, group):
        driver = self.driver
        self.open_groups_page()
        # init group creation
        driver.find_element_by_name("new").click()

        #---HACK----
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(self.username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(self.password)
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
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def login(self, username, password):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self):
        driver = self.driver
        driver.get(self.base_url + "/addressbook/")

    def destroy(self):
        self.driver.quit()