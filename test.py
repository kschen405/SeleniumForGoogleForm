from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.by import By
from random import randrange

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option("prefs", {
    "profile.password_manager_enabled": False, "credentials_enable_service": False})


url = "https://docs.google.com/forms/d/1FEITIpeubZ-K8X7oBWJ2vNgzadfiLZJ6fotS2sdNCos/viewform?edit_requested=true"
driver = webdriver.Chrome(options=option)
driver.get(url)
'''options = driver.find_elements_by_class_name(
    'quantumWizTextinputPaperinputInput')
for option in options:
    print(option)
    print("\n")'''
option_num = ['7', '11', '12', '14', '15', '16']
for i in range(6):
    options = driver.find_element_by_xpath(
        f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{option_num[i]}]')
    options = options.find_elements_by_class_name(
        "appsMaterialWizToggleRadiogroupEl")
    options[randrange(len(options))].click()
# //*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]
# //*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]

input = driver.find_elements_by_class_name(
    'quantumWizTextinputPaperinputInput')

input_array = ["youremail", "schoolmap", "somehow youremail again", "yourname",
               "phonenum", "2050", "yourschool", "test", "test", "test", "test", "test"]
for i in range(len(input)):
    input[i].clear()
    input[i].send_keys(input_array[i])

submit = driver.find_elements_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[3]/div[1]/div/span/span')

print(submit)
submit[0].click()

time.sleep(3)
driver.quit()
