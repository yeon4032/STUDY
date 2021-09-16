# -*- coding: utf-8 -*-
"""
pip install selenium
chromedriver download 버전 다운로드: https://chromedriver.chromium.org/downloads
버전 91.0.4472.164(공식 빌드) (64비트)
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlretrieve # server image -> local save
import os 
import numpy as np

pwd = os.getcwd() # 현재 경로 
print(pwd)
    

def celeb_crawler(name) : 
    # 1. dirver 경로/파일 지정 
    driver = webdriver.Chrome("C:\\ITWILL\\5_Tensoflow\\workspace\\chap07_Face_detection\\lecture00_image_crawling/chromedriver.exe")
    
    # 2. 이미지 검색 url 
    driver.get("https://www.google.co.kr/imghp?hl=ko")
    
    # 3. 검색 입력상자 tag -> 검색어 입력   
    search_box = driver.find_element_by_name('q') # element 이름 찾기 
    '''
    find_element_by_name('name') : 이름으로 element 찾기 
    find_element_by_id('id') : 아이디로 element 찾기 
    '''
    search_box.send_keys(name) # 검색어(name) 키보드 입력
    driver.implicitly_wait(3) # 3초 대기(자원 loading)
    
    # 4. [검색] 버튼 클릭 ("//tag[@attr='value']/sub element")
    driver.find_element_by_xpath("//div[@id='sbtc']/button").click() 
 
    image_url = []
     
    i=0 # 첫번째 이미지    
    base = f"//div[@data-ri='{i}']"
    driver.find_element_by_xpath(base).click() # image click
    # click image url 
    src = driver.page_source # 현재 page html source
    html = BeautifulSoup(src, "html.parser")
    img_tag = html.select("img[class='rg_i Q4LuWd']") # list
    #print(img_tag)
    
    for tag in img_tag : 
        if 'data-src' in str(tag) :
            url = tag['data-src'] # dict
            image_url.append(url)
    
    # image url 생성   
    image_url = np.unique(image_url) # 중복 url  삭제 
    print(image_url)
    
    # url -> image save
    for i in range(len(image_url)) :
        try : # 예외처리 : server file 없음 예외처리 
            file_name = "test"+str(i+1)+".jpg" # test1.jsp
            # server image -> file save
            urlretrieve(image_url[i], filename=file_name)
        except :
            print('해당 url에 image 없음 : ', i+1)        
            
    driver.close()
    


# 함수 호출 : 셀럼 이미지 저장  
namelist = ["하정우","송강호"]

for name in namelist :
    pwd = os.getcwd() # 현재 경로 
    os.mkdir(name) # 현재 위치에 폴더 생성 
    os.chdir(pwd+"/"+name) # 검색어 이용 하위폴더 생성 
    celeb_crawler(name) # image crawling
    os.chdir(pwd) # 원래 위치 이동 
    







 
    
    