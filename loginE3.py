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
url = "https://e3.nycu.edu.tw/login/index.php"

driver = webdriver.Chrome(options=option)
driver.get(url)
driver.find_element_by_xpath(
    '//*[@id="page-login-index"]/div[7]/div[1]/div[1]/div/p[3]/span[5]/b/span/span/a').click()
driver.find_element_by_xpath('//*[@id="account"]').send_keys('yourusername')
driver.find_element_by_xpath(
    '//*[@id="password"]').send_keys('yourpassword')
driver.find_element_by_xpath(
    '//*[@id="app"]/div/section[2]/div/form/input').click()
