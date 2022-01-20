from pandas import option_context
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.by import By
from random import randint, randrange, choices


option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option("prefs", {
    "profile.password_manager_enabled": False, "credentials_enable_service": False})


url = "https://docs.google.com/forms..."
driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get(url)
option_num = [1, 2, 3, 5]
for i in range(4):
    options = driver.find_element_by_xpath(
        f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{option_num[i]}]')
    options = options.find_elements_by_class_name(
        'appsMaterialWizToggleRadiogroupEl')
    if option_num[i] == 1:
        choose = choices([2, 3, 4], [0.23, 0.54, 0.23])[0]
        options[choose].click()
    elif option_num[i] == 2:
        choose = choices([0, 1], [0.83, 0.17])[0]
        options[choose].click()
    elif option_num[i] == 3:
        choose = choices([1, 2, 3, 4, 5, 6], [
                         0.04, 0.2, 0.23, 0.27, 0.17, 0.09])[0]
        options[choose].click()
    elif option_num[i] == 5:
        choose = choices([0, 2, 3, 4, 6], [
                         0.3, 0.40, 0.09, 0.06, 0.21])[0]
        options[choose].click()


inputA_array = ['電腦視覺', '數值方法', '數值', '雲原生軟體開發', '雲原生']
inputA_prob = [0.57, 0.17, 0.09, 0.06, 0.11]
inputB_array = ['電腦視覺', '數值方法', '數值', '數值方法 影像處理概論', '影像處理', '影像處理概論']
inputB_prob = [0.11, 0.26, 0.2, 0.21, 0.05, 0.17]
inputC_array = ['讓大四優先!!!', '快畢業先選課', '增加人數上限',
                '加開熱門課程', '我覺得系上應該放寬畢業要求', '拜託不要再甚麼大二優先']


input = driver.find_elements_by_class_name(
    'quantumWizTextinputPaperinputInput')
print(len(input))
for i in range(2):
    print(i)
    input[i].clear()
    if i == 0:
        ans = choices(inputA_array, inputA_prob)
        input[i].send_keys(ans)
    elif i == 1:
        ans = choices(inputB_array, inputB_prob)
        input[i].send_keys(ans)


long_input = driver.find_element_by_class_name(
    'quantumWizTextinputPapertextareaInput')
# p = randint(0, 10)
# if p < 8:
print(len(inputC_array))
choose = randint(0, len(inputC_array)-1)
long_input.send_keys(inputC_array[choose])

# time.sleep(2)
# submit = driver.find_element_by_xpath(
#     '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
# submit.click()
time.sleep(200)
driver.quit()
