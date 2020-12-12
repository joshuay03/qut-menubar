from os import getcwd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from _csv import reader


class Student:
    def __init__(self):
        self.credentials_file = ''
        self.timetable_file = ''
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Firefox(options=self.options, executable_path=getcwd() + '/geckodriver')
        self.username = ''
        self.password = ''
        self.gpa = 0  # Ouch
        self.class_list = ''
        self.units = []
        self.timetable_data = []

    def login(self):
        self.driver.get('https://qutvirtual4.qut.edu.au/group/student/home')

        time.sleep(5)

        username_field = self.driver.find_element_by_id('username')
        password_field = self.driver.find_element_by_id('password')

        username_field.send_keys(self.username)
        password_field.send_keys(self.password)

        login = self.driver.find_element_by_xpath('//*[@id="kc-login"]')
        login.click()

        time.sleep(10)

        try:
            self.gpa = self.driver.find_element_by_class_name('gpa-result-mark').get_attribute('innerHTML')
            self.class_list = self.driver.find_elements_by_class_name('cr-id ')
            for unit in self.class_list:
                self.units.append(unit.get_attribute('innerHTML'))
        finally:
            self.driver.quit()

        self.driver.quit()

    def extract_credentials(self):
        with open(self.credentials_file) as csv_file:
            csv_reader = reader(csv_file)
            for row in csv_reader:
                self.username = row[0]
                self.password = row[1]

    def extract_timetable(self):
        with open(self.timetable_file) as csv_file:
            csv_reader = reader(csv_file)
            for row in csv_reader:
                self.timetable_data.append(row)
