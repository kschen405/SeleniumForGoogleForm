from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.by import By
from random import randrange

option = webdriver.ChromeOptions()
option.add_argument("disable-infobars")
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option("useAutomationExtension", False)
option.add_experimental_option(
    "prefs",
    {"profile.password_manager_enabled": False,
        "credentials_enable_service": False},
)
url = "https://portal.nycu.edu.tw/#/login?redirect=%2F"

driver = webdriver.Chrome(options=option)
driver.get(url)

driver.find_element_by_xpath('//*[@id="account"]').send_keys("YourAccount")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("YourPassword")
port = driver.find_element_by_xpath(
    '//*[@id="app"]/div/section[2]/div/form/input')
port.click()
p = port.find_element_by_class_name("router-link-exact-active")
print(p)
# driver.find_element_by_xpath('//*[@id="pane-全部"]/div[2]/div/div[1]/a')
