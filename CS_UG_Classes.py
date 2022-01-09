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


url = "https://timetable.nycu.edu.tw/?flang=zh-tw"
driver = webdriver.Chrome(options=option)
driver.get(url)
Type = driver.find_element_by_xpath(
    '//*[@id="timetable_menu" and normalize-space(.)="EEE"]')
Ans = Type.find_elements_by_css_selector(
    '#tbl_timetable_menu > tbody > tr.fcrsdep')
print(Ans)
print(Ans.text)

# driver.find_element_by_xpath('//*[@id="fType"]/option[2]').click()
time.sleep(10)
driver.quit()
