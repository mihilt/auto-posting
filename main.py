from selenium import webdriver
import json
import time

with open('account.json') as json_file:
    json_data = json.load(json_file)
    ID = json_data["id"]
    PW = json_data["pw"]

# print(ID)
# print(PW)

browser = webdriver.Chrome()
browser.get("주소 테스트")
browser.find_element_by_xpath('//*[@id="gnb_login_button"]/span[3]').click()
