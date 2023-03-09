from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
EMAIL = 'devowoyemi123@gmail.com'
PASSWORD = 'Devowo123'



class InternetSpeedTwitterBot():
    #BOT
    def __init__(self, down, up):
        chrome = Service('C:/Users/Owoyemi/Desktop/Development Env/chromedriver.exe')
        op = webdriver.ChromeOptions()
        op.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=chrome, options=op)
        self.down = down
        self.up = up

    def get_internet_speed(self):
        self.link = 'https://www.speedtest.net/'
        self.driver.get(self.link)
        self.driver.maximize_window()
        click = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]')
        click.click()
        time.sleep(60)
        self.ITdown = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]').text

        self.ITup = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]').text
        print('LOADING UP DATA')
        return [self.ITdown, self.ITup]
        #print(f'Down: {self.ITdown}\nUP: {self.ITup}')


    def tweet_at_provider(self):
        self.link = 'https://twitter.com/i/flow/login'
        self.driver.get(self.link)
        self.driver.maximize_window()
        time.sleep(2)
        self.email = self.driver.find_element(By.NAME, 'text').send_keys(EMAIL)
        self.submit = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
        time.sleep(2)
        self.password = self.driver.find_element(By.NAME, 'password').send_keys(PASSWORD)

        self.log = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]').click()
        time.sleep(10)
        tweet = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]')
        tweet.send_keys("Hello World")


bot = InternetSpeedTwitterBot(PROMISED_DOWN,PROMISED_UP)
item = bot.get_internet_speed()
print(item)







