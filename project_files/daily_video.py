from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime, timedelta
from pymongo import MongoClient

client = MongoClient("mongodb://readwrite:t01rw@localhost:27017/")
db = client.project

url = 'https://www.youtube.com/results?search_query=vegan+recipe&sp=CAMSBAgCEAE%253D'

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)
sleep(3)

# 24시간 이내에 올라온 비건 레시피 동영상 저장
for i in range(5):
    v_dict = dict()
    v_path = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer[' + str(i + 1) + ']/div[1]/div/div[1]/div/h3/a'
    v_link = driver.find_element(By.XPATH, v_path).get_attribute("href")

    if "shorts" not in v_link:
        v_dict['link'] = v_link.replace('/watch?v=', '/embed/')
    else:
        v_dict['link'] = v_link.replace('shorts', 'embed')
    
    v_dict['created_at'] = datetime.now().astimezone().isoformat()

    db.youtube.insert_one(v_dict)
    print(v_dict)
    

# 1주일 이전에 저장된 링크 삭제
now = datetime.now()
week_ago = now - timedelta(days=7)

db.youtube.delete_many({"created_at": {"$lte": week_ago.isoformat()}})
