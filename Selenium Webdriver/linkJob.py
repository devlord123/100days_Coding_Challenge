from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome = Service('C:/Users/Owoyemi/Desktop/Development Env/chromedriver.exe')
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=chrome, options=op)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3499206152&f_LF=f_AL&geoId=102257491&keywords=python'
           '%20developer&location=London%2C%20England%2C%20United%20Kingdom')


##############---------AUTHOMATE LOGIN-----------########################

log = driver.find_element(By.CSS_SELECTOR, '.nav__button-secondary')
log.click()

email = driver.find_element(By.NAME, 'session_key')
email.send_keys('owoyemiidrisolamilekan@gmail.com')
password = driver.find_element(By.NAME, 'session_password')
password.send_keys('Devowo123')
button = driver.find_element(By.CSS_SELECTOR, '.btn__primary--large')
button.click()

##################-------AUTHOMATE APPLICATION----------#####################

time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR,"button #ember814")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(By.CLASS_NAME,"fb-single-line-text__input")
if phone.text == "":
    phone.send_keys('90738278920')

#Submit the application
submit_button = driver.find_element(By.CLASS_NAME, "footer button")
submit_button.click()
