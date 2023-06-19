## 총 44개 수집됨
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

from selenium_sets import selenium_sets
from cat_link import BASE_URL, link_dict
import json

driver = selenium_sets()

# 창 크기 조절 코드 추가
driver.set_window_size(1920, 1080)  # 창 크기 조절. 여기서 너비는 1920px, 높이는 1080px로 설정되어 있습니다.

# item/new scrap    
driver.get(BASE_URL + link_dict['new'])
time.sleep(3) # 웹 페이지 로딩으로 인한 오류 및 서버 과부하 방지를 위해 3초간 프로세스를 일시 정지합니다.

prdlist = driver.find_elements(By.CLASS_NAME, 'prdList')
box_list = prdlist[1].find_elements(By.CLASS_NAME, 'box')
item_info = []
for box in box_list: # 상품 박스 마다 (이미지: {}, 상품이름: {}, 상품 가격: {}, 구매링크: {})
    item_dict = {}
    # 상품 이름
    name = box.find_element(By.CLASS_NAME, 'name')
    name_raw = name.text
    # 상품 가격
    list_item = box.find_element(By.CLASS_NAME, 'xans-product-listitem')
    li_list = list_item.find_elements(By.CLASS_NAME, 'xans-record-')
    item_price = li_list[1].text
    # 구매 링크
    item_link = name.find_element(By.TAG_NAME, 'a').get_attribute('href')
    # 상품 이미지
    thumb = box.find_element(By.CLASS_NAME, 'thumbnail')
    item_img = thumb.find_element(By.TAG_NAME, 'img').get_attribute('src')
    
    # 딕셔너리에 추가
    item_dict['item_name'] = name_raw.split('\n')[0]
    try:
        item_dict['item_price'] = item_price.split()[0] # 할인가 적힌 경우
    except:
        item_dict['item_price'] = item_price
    item_dict['item_link'] = item_link
    item_dict['item_img'] = item_img
    
    # 리스트에 추가
    item_info.append(item_dict)
# 드라이버 종료
driver.quit()

with open('./data/item_new.json', 'w', encoding='utf-8') as file:  
    json.dump(item_info, file, ensure_ascii=False, indent=2)
