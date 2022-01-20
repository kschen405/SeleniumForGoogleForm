from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from random import randrange
import time

option = webdriver.ChromeOptions()
option.add_argument("disable-infobars")
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option("useAutomationExtension", False)
option.add_experimental_option(
    "prefs",
    {"profile.password_manager_enabled": False, "credentials_enable_service": False},
)
option.add_argument("--ignore-certificate-errors")
option.add_argument("--start-maximized")


url = "https://timetable.nycu.edu.tw/?flang=zh-tw"
driver = webdriver.Chrome(options=option)
driver.get(url)
table = driver.find_element_by_id("tbl_timetable_menu")
rows = table.find_elements_by_tag_name("tr")
print(len(rows))
print(rows[1])
print(rows[1].text)
for row in rows:
    for td in rows:
        print(td)
# rows[1].click()
# ans = driver.find_element_by_xpath('//*[@id="fType"]/option[1]').click()
# driver.find_element_by_xpath('//*[@id="fType"]/option[2]').click()
time.sleep(10)
driver.quit()
