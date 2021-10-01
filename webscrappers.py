from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart

from selenium.webdriver.remote.webelement import WebElement

def send_keys(el: WebElement, keys: str):
    for i in range(len(keys)):
        el.send_keys(keys[i])


browser = webdriver.Safari(executable_path='/usr/bin/safaridriver')
browser.get('https://www.yatra.com') 
time.sleep(1)
origin = browser.find_element(By.ID, "BE_flight_origin_city")
origin.clear()
time.sleep(1.5)
origin.send_keys(' '+ "BLR")
origin.send_keys(Keys.ENTER)
time.sleep(1.5)
destination = browser.find_element(By.ID, "BE_flight_arrival_city")
destination.clear()
time.sleep(1.5)
destination.send_keys(' '+ "MAA")
destination.send_keys(Keys.ENTER)
time.sleep(1.5)
searchbutton = browser.find_element(By.ID,"BE_flight_flsearch_btn")
searchbutton.click()
date = browser.find_element(By.ID, "BE_flight_origin_date")
date.click()
date.send_keys(Keys.CONTROL, "a") # Select all pre-existing text/input value
date.send_keys(Keys.BACKSPACE)
date.send_keys("19/09/2021")
date.click()
time.sleep(1)
searchbutton = browser.find_element(By.ID,"BE_flight_flsearch_btn")
searchbutton.click()
time.sleep(1)

print('Results ready!')