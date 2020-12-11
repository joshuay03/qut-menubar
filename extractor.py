from os import getcwd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from _csv import reader


class Student:
    def __init__(self):
        self.credentials = ''
        self.timetable = ''
        self.gpa = 0  # Ouch
        self.rows = []
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Firefox(options=self.options, executable_path=getcwd() + '/geckodriver')

    def login(self):
        self.driver.get('https://qutvirtual4.qut.edu.au/group/student/home')

        with open(self.credentials) as csv_file:
            csv_reader = reader(csv_file)
            for row in csv_reader:
                username = row[0]
                password = row[1]

        time.sleep(5)

        username_field = self.driver.find_element_by_id('username')
        password_field = self.driver.find_element_by_id('password')

        username_field.send_keys(username)
        password_field.send_keys(password)

        login = self.driver.find_element_by_xpath('//*[@id="kc-login"]')
        login.click()

        time.sleep(5)

    def extract_gpa(self):
        self.gpa = self.driver.find_element_by_class_name('gpa-result-mark').get_attribute('innerHTML')
        self.driver.close()

    def extract_timetable(self):
        with open(self.timetable) as csv_file:
            csv_reader = reader(csv_file)
            for row in csv_reader:
                self.rows.append(row)
