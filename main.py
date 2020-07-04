from selenium import webdriver
import json
import time

#네이버 카페 주소 바로 입력 기준이다

with open("secret/account.json") as json_file:
    json_data = json.load(json_file)
    data_id = json_data["id"]
    data_pw = json_data["pw"]
    data_address = json_data["address"]


#저장된 account 확인
# print(data_id)
# print(data_pw)
# print(data_address)

###################################

#실행
driver = webdriver.Chrome()
driver.get(data_address)
driver.find_element_by_xpath('//*[@id="gnb_login_button"]/span[3]').click()

driver.find_element_by_name('id').send_keys(data_id)
time.sleep(1)
driver.find_element_by_name('pw').send_keys(data_pw)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="log.login"]').click()

# 일단 오늘 여기서 네이버 캡챠가 떠버림..