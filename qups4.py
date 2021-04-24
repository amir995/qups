from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#
import time
import re
my_options = webdriver.ChromeOptions()
#my_options.add_argument('--no-sandbox')
#my_options.add_argument("--kiosk")
#my_options.add_argument("--headless")
#my_options.add_argument("--incognito")

user_id = "01834085818"
user_pass = "162-15-8178"

driver = webdriver.Chrome("chromedriver.exe", chrome_options=my_options)
driver.maximize_window()

driver.get("https://evaly.com.bd/career")

time.sleep(1)
#To remove popup ad
if driver.find_element_by_xpath("//button[@class='absolute top-0 right-0 p-2 text-white']"):
    driver.find_element_by_xpath("//button[@class='absolute top-0 right-0 p-2 text-white']").click()
else:
    pass


titles = driver.find_elements_by_xpath("//div/h3[@class='mb-0 font-semibold']")
for title in titles:
    title = title.text
    driver.find_element_by_xpath("//div/h3[contains(text(),'"+ title +"')]").click()
emails = driver.find_elements_by_xpath("//p/a[@class='text-blue-500']")

email_ls = []
for email in emails:
    email_ls.append(email.text[-13:])

validation = "valid"
for email in email_ls:
    if email!= "@evaly.com.bd":
        validation = "invalid"
print("Validation: Each Domain name is "+ validation)
