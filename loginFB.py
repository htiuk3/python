import argparse
import sys
import time
from selenium import webdriver
from random import randint

def random_sleep(min_s, max_s):
    time.sleep(randint(min_s, max_s))

FB_URL = "https://facebook.com"

myUsername = "williamdat10@gmail.com"
myPassword = "Thanghekhoc@1"

browser = webdriver.Chrome()
browser.get(FB_URL)
random_sleep(2, 3)

usernameSelector = '#email'
passwordSelector = '#pass'
btnLoginSelector = '#u_0_b'

usernameInput = browser.find_element_by_css_selector(usernameSelector)
passwordInput = browser.find_element_by_css_selector(passwordSelector)
btnLogin = browser.find_element_by_css_selector(btnLoginSelector)

usernameInput.send_keys(myUsername)
random_sleep(1, 3)
passwordInput.send_keys(myPassword)
random_sleep(1, 3)
btnLogin.click()

