from _csv import reader
from selenium import webdriver


def bb_login():
    driver = webdriver.Safari()
    driver.get('https://esoe.qut.edu.au/auth/realms/qut/protocol/openid-connect/auth?response_type=code&client_id=shibboleth-2-idp&redirect_uri=https%3A%2F%2Fidp.qut.edu.au%2Fidp%2Fprofile%2FSAML2%2FPOST%2FSSO?execution%3De5s1%26_eventId_proceed%3D1&state=228096%2F235063b5-dfc0-4ddc-b105-b4ac85010379&scope=openid')

    username = driver.find_element_by_id('username')
    password = driver.find_element_by_id('password')

    username.send_keys('n10404074')
    password.send_keys('Naruto19ro99%')

    login = driver.find_element_by_xpath('//*[@id="kc-login"]')
    login.click()


def extract_timetable(timetable_file):
    with open(timetable_file) as csv_file:
        csv_reader = reader(csv_file)
        rows = []
        for row in csv_reader:
            rows.append(row)

    return rows


if __name__ == '__main__':
    bb_login()
