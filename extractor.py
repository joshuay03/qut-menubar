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

        with open('credentials.csv') as csv_file:
            csv_reader = reader(csv_file)
            for row in csv_reader:
                username = row[0]
                password = row[1]

        username_field = driver.find_element_by_id('username')
        password_field = driver.find_element_by_id('password')

        username_field.send_keys(username)
        password_field.send_keys(password)

        login = driver.find_element_by_xpath('//*[@id="kc-login"]')
        login.click()
        time.sleep(7.5)

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
