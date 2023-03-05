from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome = Service('C:/Users/Owoyemi/Desktop/Development Env/chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome, options=op)
driver.get("https://www.python.org")
times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

data = {}

for i in range(len(times)):
    data[i] = {
        'time': times[i].text,
        'name': names[i].text

    }

print(data)
driver.quit()
