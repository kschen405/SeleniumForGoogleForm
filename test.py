from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option("prefs", {
    "profile.password_manager_enabled": False, "credentials_enable_service": False})


url = "https://docs.google.com/forms/d/1FEITIpeubZ-K8X7oBWJ2vNgzadfiLZJ6fotS2sdNCos/viewform?edit_requested=true"
driver = webdriver.Chrome(options=option)
driver.get(url)
option = driver.find_elements_by_class_name(
    'appsMaterialWizToggleRadiogroupEl')


option_status = option[2]
option_status.click()

'''
nextbtn = driver.find_elements_by_class_name('appsMaterialWizButtonEl')[1]
nextbtn.click()
option = driver.find_elements_by_class_name(
    'appsMaterialWizToggleRadiogroupEl')

option_status = option[1]
option_status.click()
'''

input = driver.find_elements_by_class_name(
    'quantumWizTextinputPaperinputInput')

input_array = ["map", "email.com", "myname",
               "phone num", "2502", "785225", "7278587", "8532572", "none", "OHHHHHHHH", "test"]
for i in range(len(input)):
    input[i].clear()
    input[i].send_keys(input_array[i])

time.sleep(10)
driver.quit()
