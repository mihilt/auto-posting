from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time
import pyperclip

with open("secret/data.json") as json_file:
    json_data = json.load(json_file)
    data_id = json_data["id"]
    data_pw = json_data["pw"]

    data_address = json_data["address"] #카페 대문 주소

    data_category_choice = json_data["category_choice"]  # 게시판 콤보박스 요소 선택
    data_post_subject = json_data["post_subject"] #게시글 제목




#저장된 account 확인
# print(data_id)
# print(data_pw)
# print(data_address)

###################################

#실행
driver = webdriver.Chrome()
driver.get(data_address)
driver.find_element_by_xpath('//*[@id="gnb_login_button"]/span[3]').click()

# driver.find_element_by_name('id').send_keys(data_id)
pyperclip.copy(data_id)
# driver.find_element_by_name('id').click()
driver.find_element_by_name('id').send_keys(Keys.CONTROL, 'v')

time.sleep(1)
# driver.find_element_by_name('pw').send_keys(data_pw)
pyperclip.copy(data_pw)
# driver.find_element_by_name('pw').click()
driver.find_element_by_name('pw').send_keys(Keys.CONTROL, 'v')

time.sleep(1)
driver.find_element_by_xpath('//*[@id="log.login"]').click()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="cafe-info-data"]/div[2]/a').click()

#게시판 선택
driver.find_element_by_xpath('//*[@id="boardCategory"]/option[text()=' + data_category_choice + ']').click()

# 제목입력
driver.find_element_by_name('subject').send_keys(data_post_subject)


#캡챠 해결, JSON 한글 파싱 오류 생김