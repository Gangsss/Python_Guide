import time
import random
from selenium import webdriver
from urllib.parse import quote
from selenium.common.exceptions import NoSuchElementException
import request
from bs4 import BeautifulSoup


id = 'id'
password = 'password'

timeline_like_count = 80
hash_tags = ['안암','건대','보아즈']
hash_tags_count = 120
location = ['서울, 서울역, 건대입구역']

browser = webdriver.Chrome('C:/Users/Kim/Desktop/chromedriver')

browser.implicitly_wait(3)

browser.get('https://instagram.com/')

browser.implicitly_wait(3)

login_link = browser.find_element_by_css_selector('p.izU2O').find_element_by_css_selector('a')
login_link.click()

time.sleep(3) # login 함수가 먹히는 거 방지
#wait.until(ExpectedConditions.stalenessOf(whatever element)); 이런 것도 있다고 한다
#https://stackoverflow.com/questions/40029549/how-to-avoid-staleelementreferenceexception-in-selenium-python


def login(id, password):
    #로그인 안되었을 때 어떻게 해야할까?
    input = browser.find_elements_by_css_selector("input._2hvTZ") #변수정리
    
    id_input=input[0]
    id_input.send_keys(id)
    
    browser.implicitly_wait(3)
    
    pass_input=input[1]
    pass_input.send_keys(password)
    
    browser.find_element_by_css_selector('button._5f5mN').click()
    
    print("로그인 완료")   
    print('-'*20)
    
    time.sleep(3)
    

def timeline_like(timeline_like_count):
    
    browser.get('https://www.instagram.com/') # 다른 화면에서 일단 인스타그램 피드로
    for i in range(timeline_like_count):
        try:
            heart_buttons = browser.find_elements_by_css_selector('span.fr66n')
            button= heart_buttons[i].find_element_by_css_selector('button')
            likebutton= button.find_element_by_css_selector('span.glyphsSpriteHeart__outline__24__grey_9.u-__7')
            likebutton.click()
                
        except NoSuchElementException:
            print("피드의 " +str(i+1)+"번째 사진은 이미 좋아요가 눌려있습니다.")
         
                 
        except IndexError:     #index error 피하기 위해 tryexcept문 사용
            print("더 이상 사진이 없습니다.")
    
    browser.implicitly_wait(2)
    print('-'*20)
         
           
def hash_tags_like(hash_tags, hash_tags_count):
    for i in range(len(hash_tags)):
        browser.get("https://www.instagram.com/explore/tags/"+hash_tags[i]+"/")
        time.sleep(3) # 천천히 들어가기 막히는 거 방지
        for k in range(hash_tags_count):
            photos=browser.find_elements_by_css_selector("div._9AhH0")
            photos[k].click()
            
            browser.implicitly_wait(3)
            try:
                heart = browser.find_element_by_css_selector('span.fr66n')
                button= heart.find_element_by_css_selector('button')
                # html코드에 띄어쓰기가 있을 시 .으로 채워준다
                # 'glyphsSpriteHeart__filled__24__red_5 u-__7' ->‘glyphsSpriteHeart__filled__24__red_5.u-__7’
                likebutton= button.find_element_by_css_selector('span.glyphsSpriteHeart__outline__24__grey_9.u-__7')

                likebutton.click()
                
            except NoSuchElementException:
                # NoSuchElementException을 적용하기 위해서는
                # from selenium.common.exceptions import NoSuchElementException을 해야한다.
                print("#"+hash_tags[i]+"의 "+str(k+1)+"번째 사진은 이미 좋아요가 눌려있습니다.")
                
            
            except IndexError:    
                print("더 이상 사진이 없습니다.")
            
            browser.implicitly_wait(2)
        
            close = browser.find_element_by_xpath("/html/body/div[3]/div/button")
            close.click()
            
            browser.implicitly_wait(2)
            
    print('-'*20)
    print('끝났습니다~')

def search_by_loc(location):
    for i in range(len(location)):
        browser.get('https://www.instagram.com')
        time.sleep(3)
        browser.set_window_size(1024, 600) # 페이지가 어느정도 커야 검색 창이 보이므로 고정 시킨다.
        time.sleep(2)
        # 반복시 검색어가 쌓인다. 이를 방지하기 위해 처음에 검색어 삭제버튼을 누르기 
        browser.find_element_by_css_selector('div.pbgfb.Di7vw ').click()
        time.sleep(2)
        browser.find_element_by_css_selector('div.aIYm8.coreSpriteSearchClear').click()
        time.sleep(2)
        browser.find_element_by_css_selector("input.XTCLo.x3qfX ").send_keys(location[i])
        time.sleep(2)
            
        html= browser.page_source
        soup = BeautifulSoup(html,'html.parser')
        page_all = soup.select('a.yCE8d')

        # 위치는 태그로 검색하는 것과 다르게 #이 붙어 있지않다. 
        # .text()를 이용해 tag안의 텍스트를 가져오고 그것이 location 이 같으면
        # href에 있는 주소를 가져다가 쓴다.
        url =''
    
        for page in page_all:
            if page.text == location:
                url+= page.get('href')
                print('검색한 '+location[i]+'이(가) 위치로 등록 되어있습니다.')
        if url =='':
            print('검색한 '+ location[i] + '이(가) 위치로 등록이 안되어있습니다.')
             


login(id, password)
timeline_like(timeline_like_count)
hash_tags_like(hash_tags, hash_tags_count)
search_by_location(location)

browser.quit()

