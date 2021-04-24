from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#
import time
import re
my_options = webdriver.ChromeOptions()
my_options.add_argument('--no-sandbox')
#my_options.add_argument("--headless")


user_id = "01834085818"
user_pass = "162-15-8178"

driver = webdriver.Chrome("chromedriver.exe", chrome_options=my_options)
driver.maximize_window()

driver.get("https://evaly.com.bd/")



time.sleep(1)
#To remove popup ad
if driver.find_element_by_xpath("//button[@class='absolute top-0 right-0 p-2 text-white']"):
    driver.find_element_by_xpath("//button[@class='absolute top-0 right-0 p-2 text-white']").click()
else:
    pass



#Login
login_element = driver.find_element_by_xpath("//span[@class='p-2 bg-white rounded-full shadow']").click()

time.sleep(2)
driver.implicitly_wait(10) # seconds
driver.find_element_by_name("phone").send_keys(user_id)
driver.find_element_by_name("password").send_keys(user_pass+Keys.RETURN)

time.sleep(2.5)
#Speaker element clicking
#driver.find_element_by_xpath("//ul//li//a//span/a[@href='/categories/speaker-2f615cf9a']").click()
driver.find_element_by_xpath("//a/span[contains(text(),'Speaker')]").click()

driver.implicitly_wait(10)
brands  = driver.find_elements_by_xpath("//div/p[@class='BrandCard___StyledP-sc-1kq2v0k-1 bAWFRI text-sm font-semibold text-center cursor-pointer']")

number_of_brands = len(brands)

with open('Brand Data.txt', 'a',encoding="utf-8") as f:
        f.write("Total Brands = "+str(number_of_brands)+"\n\n")

trac1=[]
for brand in brands:
    #print(brand.text)
    if brand not in trac1:
        with open('Brand Data.txt', 'a',encoding="utf-8") as f:
            f.write(brand.text+"\n")
        trac1.append(brand)
    else:
        pass
print("task-1 DONE.")
