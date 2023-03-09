from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome = Service('C:/Users/Owoyemi/Desktop/Development Env/chromedriver.exe')
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=chrome, options=op)
driver.get('https://www.google.com/')


search = driver.find_element(By.NAME, 'q')
search.send_keys('Unibadan')
search.send_keys(Keys.ENTER)

first_link = driver.find_element(By.CSS_SELECTOR, '.yuRUbf a')
first_link.click()



# email = driver.find_element(By.NAME, 'email')
# email.send_keys("owoyemiidrisolamilekan@gmail.com")
# password = driver.find_element(By.NAME, 'password')
# password.send_keys("12345??")
# button = driver.find_element(By.CSS_SELECTOR, '.ant-btn')
# button.click()





# figure = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
#
# search = driver.find_element(By.NAME, 'search')
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

