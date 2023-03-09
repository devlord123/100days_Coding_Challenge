from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
link = 'https://coinmarketcap.com/'
chrome = Service('C:/Users/Owoyemi/Desktop/Development Env/chromedriver.exe')
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=chrome, options=op)
driver.get(link)

time.sleep(2)

nav = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[1]/div[2]/div/nav/div/div[5]')
nav.click()

time.sleep(2)
login = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div')

print(login)



# log = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[1]/button')
# log.click()



############-------LOGIN------------#########

# time.sleep(5)
# email = driver.find_element(By.NAME, 'email')
# email.send_keys("owoyemiidrisolamilekan123@gmail.com")
# password = driver.find_element(By.NAME, 'pass')
# password.send_keys('Owo123??')
#
# button = driver.find_element(By.NAME, 'login')
# button.click()

# time.sleep(5)





