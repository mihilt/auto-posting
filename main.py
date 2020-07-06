from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time
import pyperclip

with open("secret/data.json", "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)
    data_id = json_data["id"]
    data_pw = json_data["pw"]

    data_address = json_data["address"] #카페 대문 주소

    # data_category_choice = json_data["category_choice"]  # 게시판 콤보박스 요소 선택
    data_post_subject = json_data["post_subject"] #게시글 제목

    data_category_xpath = json_data["category_xpath"]




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


# 게시글 작성 바로클릭
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="cafe-info-data"]/div[2]/a').click()

# 게시판에 들어간 이후 나오는 게시글 작성 버튼 해보자
time.sleep(1)
driver.find_element_by_xpath(data_category_xpath).click()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="cafe-info-data"]/div[2]/a').click()

print(data_post_subject)

# 제목입력
# pyperclip.copy(data_post_subject)
# driver.find_element_by_xpath('//*[@id="subject"]').click()
# driver.find_element_by_xpath('//*[@id="subject"]').clear()
# driver.find_element_by_xpath('/html/body/form[1]/div[1]/div[1]/div/ul[1]/li[2]/div/input').send_keys(Keys.CONTROL, 'v')
# driver.find_elements_by_id("subject").send_keys("test")
# print(driver.find_elements_by_id("subject"))
# print(driver.find_element_by_xpath('/html/body'))
# print(driver.find_element_by_xpath('//*[@id="boardCategory"]'))

# driver.find_element_by_xpath('/html/body').send_keys("test")

#게시판 선택
# driver.find_element_by_xpath("//*[@id='boardCategory']/option[text()='" + data_category_choice + "']").click()

# # 제목입력
# driver.find_element_by_name('subject').send_keys(data_post_subject)



#일단 제목 복사해놓기
pyperclip.copy(data_post_subject)


# JSON 한글 파싱 오류해결
# 카테고리 설정까지 가능, 제목은 접근조차 안되며, 내용은 왜그런지 함수가 안먹음, 제목 복붙 시작부터는 아직까지 수작업 필요


