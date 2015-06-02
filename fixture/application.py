__author__ = 'Lenusik'
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

        self.username = "admin"
        self.password = "secret"

    def open_home_page(self):
        driver = self.driver
        driver.get(self.base_url + "/addressbook/")

    def destroy(self):
        self.driver.quit()