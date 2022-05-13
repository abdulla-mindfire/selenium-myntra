from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import time

url = 'https://www.myntra.com/'

options = Options() 
# options.headless = True # Set true for headless

# Add args to use default chrome profile for already logged in sessions
options.add_argument('--profile-directory=Profile 1')
options.add_argument("user-data-dir=home/abdulla/.config/google-chrome/Default") 
driver = webdriver.Chrome(options=options)

# driver.delete_all_cookies()

driver.implicitly_wait(5)

driver.maximize_window()

# Directing the driver to the defined url
driver.get(url)
time.sleep(5)

# Initialize ActionChain to perform any action over webpage
action = ActionChains(driver)


menu1 = driver.find_element(by=By.CLASS_NAME, value='desktop-userIconsContainer')
action.move_to_element(menu1).perform()

n = driver.find_elements(by=By.CLASS_NAME, value='desktop-linkButton')

if len(n) > 0:
    print("enter")
    action.move_to_element(n[0]).click().perform()
    # entering details like number to hit login

    phone_number = "8317081491"

    driver.find_element(by=By.CLASS_NAME, value='mobileNumberInput').send_keys(phone_number)
    time.sleep(5)

    driver.find_element(by=By.CLASS_NAME, value='submitBottomOption').click()
    time.sleep(5)

    otpVerification = driver.find_elements(by=By.CLASS_NAME, value='verificationContainer')

    if len(otpVerification) == 0:
        print("otp ")
        time.sleep(32)
        driver.find_element(by=By.CLASS_NAME, value='submitBottomOption').click()

    time.sleep(40)
    driver.implicitly_wait(20)

menu = driver.find_element(by=By.CLASS_NAME, value='desktop-userIconsContainer')
action.move_to_element(menu).perform()
time.sleep(3)

# Xpath to click over saved addresses
path = '//*[@id="desktop-header-cnt"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/a[4]'

address = driver.find_element(by=By.XPATH, value=path).click()

time.sleep(3)

address = driver.find_elements(by=By.CLASS_NAME, value='addressAccordian-myAddress')

lst = []

for idx, add in enumerate(address):
    try:
        lst.append(add.text)
    except:
        continue

mydct = {}

for idx, i in enumerate(lst):
    data = i.split('\n')
    new_lst = []
    for ad in data:
        if ad not in ['HOME', 'EDIT', 'REMOVE', 'MAKE THIS DEFAULT']:
            new_lst.append(ad)
    mydct[f"{idx}"] = new_lst
    new_lst = []

print(mydct)


driver.quit()

