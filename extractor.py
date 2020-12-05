from os import getcwd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from _csv import reader


class Student:
    def __init__(self):
        self.gpa = 0  # Ouch

    def login(self):
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options, executable_path=getcwd()+'/geckodriver')

        driver.get('https://qutvirtual4.qut.edu.au/group/student/home')
        time.sleep(3)

        username = driver.find_element_by_id('username')
        password = driver.find_element_by_id('password')

        username.send_keys('n10404074')
        password.send_keys('DJRY030699#')

        login = driver.find_element_by_xpath('//*[@id="kc-login"]')
        login.click()
        time.sleep(5)

        self.gpa = driver.find_element_by_class_name('gpa-result-mark').get_attribute('innerHTML')


def extract_timetable(timetable_file):
    with open(timetable_file) as csv_file:
        csv_reader = reader(csv_file)
        rows = []
        for row in csv_reader:
            rows.append(row)

    return rows


if __name__ == '__main__':
    Student().login()
