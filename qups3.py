from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

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


driver.implicitly_wait(10)
driver.find_element_by_name("phone").send_keys(user_id)
driver.find_element_by_name("password").send_keys(user_pass+Keys.RETURN)

time.sleep(2)
driver.find_element_by_xpath("//div/input[@aria-autocomplete='both']").send_keys("motor bike"+Keys.RETURN)

inp1 = driver.find_element_by_xpath("//form/input[@placeholder='Min price']")
inp1.clear()
inp1.send_keys("90000")

inp2 = driver.find_element_by_xpath("//form/input[@placeholder='Max price']")
inp2.clear()
inp2.send_keys("200000"+Keys.RETURN)


driver.find_element_by_xpath("//label/span[contains(text(),'Motor Bike')]").click()


bike_brand = "TVS"
check_box = driver.find_element_by_xpath("//label/span[contains(text(),'"+bike_brand+"')]")
check_box.click()


color = "Blue"
driver.find_element_by_xpath("//label/span[contains(text(),'"+color+"')]").click()


#clicking on TVS Bike Card
driver.find_element_by_xpath("//div/p[contains(text(),'Tvs Auto Bangladesh Ltd')]").click()


bike_brand2 = str(driver.find_element_by_xpath("//span/a[contains(text(),'TVS')]").text)
#print(bike_brand2)
############Validation##########
if bike_brand==bike_brand2:
    print("Validation 1: brand name " +bike_brand2+" is valid")
else:
    print("Validation 1: brand name " +bike_brand2+" is invalid")


driver.implicitly_wait(10) # seconds
#select 4 bikes
driver.find_element_by_xpath("//button/span[contains(text(),'Only 1')]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//div/p[contains(text(),'Only 4')]").click()



#No shop found releated to this product
