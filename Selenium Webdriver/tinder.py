from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
link = 'https://tinder.com/'
chrome = Service('C:/Users/Owoyemi/Desktop/Development Env/chromedriver.exe')
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=chrome, options=op)
driver.get(link)
driver.maximize_window()

log = driver.find_element(By.LINK_TEXT, 'Log in')
log.click()

time.sleep(2)
facebook = driver.find_element(By.XPATH, '//*[@id="o1622039657"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]').click()

###########-------------LOGIN------------#################################
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

print(f'Loading up {driver.title}')



time.sleep(2)
email = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('owoyemiidrisolamilekan123@gmail.com')
password = driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys('Owo123??')
fb_log = driver.find_element(By.NAME, 'login').click()
time.sleep(5)
driver.switch_to.window(base_window)
time.sleep(10)
pop1 = driver.find_element(By.XPATH, '//*[@id="o1622039657"]/main/div/div/div/div[3]/button[1]/div[2]').click()
time.sleep(1)
pop2 = driver.find_element(By.XPATH, '//*[@id="o1622039657"]/main/div/div/div/div[3]/button[1]').click()
time.sleep(1)
cookies = driver.find_element(By.XPATH, '//*[@id="o1400699221"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]').click()

time.sleep(15)
likes = driver.find_element(By.XPATH, '//*[@id="o1400699221"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button').click()
time.sleep(3)