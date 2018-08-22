import time
import random
from selenium import webdriver
from urllib.parse import quote


id = 'id'
password = 'password'

timeline_like_count = 120
hash_tags = ['코딩', '빅데이터','보아즈']
hash_tags_count = 60

browser = webdriver.Chrome('C:/Users/Kim/Desktop/chromedriver')

browser.implicitly_wait(3)

browser.get('https://instagram.com/')

browser.implicitly_wait(3)

login_link = browser.find_element_by_css_selector('p.izU2O').find_element_by_css_selector('a')
login_link.click()

def login(id, password):
    
    id_input=browser.find_elements_by_css_selector("input._2hvTZ")[0]
    id_input.send_keys(id)
    
    browser.implicitly_wait(3)
    
    pass_input=browser.find_elements_by_css_selector("input._2hvTZ")[1]
    pass_input.send_keys(password)
    
    browser.find_element_by_css_selector('button._5f5mN').click()
    
    pass

def timeline_like(timeline_like_count):
    for i in range(timeline_like_count):
        Button_like=browser.find_elements_by_css_selector('span.fr66n')[i].find_element_by_css_selector   ('button')
        Button_like.click()
    pass

def hash_tags_like(hash_tags, hash_tags_count):
    '''
    해시태그 좋아요 구현
    '''
    pass


login(id, password)
timeline_like(timelinke_like_count)
hash_tags_like(hash_tags, hash_tags_count)

browser.quit()