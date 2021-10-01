from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart

from selenium.webdriver.remote.webelement import WebElement




browser = webdriver.Safari(executable_path='/usr/bin/safaridriver')
browser.get('https://www.yatra.com') 
time.sleep(1)
hotel = browser.find_element(By.ID, "booking_engine_hotels")
hotel.click()
time.sleep(1)
destination = browser.find_element(By.ID, "BE_hotel_destination_city")
destination.clear()
destination.send_keys("Goa")
time.sleep(1.5)
destination.send_keys(Keys.ENTER)
destination.click()
time.sleep(2)
searchbtn = browser.find_element(By.ID, "BE_hotel_htsearch_btn")
searchbtn.click()
time.sleep(1)

print('Results ready!')