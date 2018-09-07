import time
import random
from selenium import webdriver
from urllib.parse import quote
from selenium.common.exceptions import NoSuchElementException
import request
from bs4 import BeautifulSoup



timeline_like_count = 80
hash_tags = ['�Ⱦ�','�Ǵ�','������']
hash_tags_count = 120
location = ['����, ���￪, �Ǵ��Ա���']

browser = webdriver.Chrome('C:/Users/Kim/Desktop/chromedriver')

browser.implicitly_wait(3)

browser.get('https://instagram.com/')

browser.implicitly_wait(3)

login_link = browser.find_element_by_css_selector('p.izU2O').find_element_by_css_selector('a')
login_link.click()

time.sleep(3) # login �Լ��� ������ �� ����
#wait.until(ExpectedConditions.stalenessOf(whatever element)); �̷� �͵� �ִٰ� �Ѵ�
#https://stackoverflow.com/questions/40029549/how-to-avoid-staleelementreferenceexception-in-selenium-python



## Ŭ����ȭ __init__ �޼��� �̿�-> �α����� �ٷ� �� �� �ְ�


class auto_insta:
    def __init__(self, id, password):
        
        self.id = id
        self.password= password

        input = browser.find_elements_by_css_selector("input._2hvTZ") #��������

        id_input=input[0]
        id_input.send_keys(self.id)

        browser.implicitly_wait(3)

        pass_input=input[1]
        pass_input.send_keys(self.password)

        browser.find_element_by_css_selector('button._5f5mN').click()

        print("�α��� �Ϸ�")   
        print('-'*20)

        time.sleep(3)


    def timeline_like(self,timeline_like_count):

        browser.get('https://www.instagram.com/') # �ٸ� ȭ�鿡�� �ϴ� �ν�Ÿ�׷� �ǵ��
        for i in range(timeline_like_count):
            try:
                heart_buttons = browser.find_elements_by_css_selector('span.fr66n')
                button= heart_buttons[i].find_element_by_css_selector('button')
                likebutton= button.find_element_by_css_selector('span.glyphsSpriteHeart__outline__24__grey_9.u-__7')
                likebutton.click()

            except NoSuchElementException:
                print("�ǵ��� " +str(i+1)+"��° ������ �̹� ���ƿ䰡 �����ֽ��ϴ�.")


            except IndexError:     #index error ���ϱ� ���� tryexcept�� ���
                print("�� �̻� ������ �����ϴ�.")

        browser.implicitly_wait(2)
        print('-'*20)


    def hash_tags_like(self,hash_tags, hash_tags_count):
        for i in range(len(hash_tags)):
            browser.get("https://www.instagram.com/explore/tags/"+hash_tags[i]+"/")
            time.sleep(3) # õõ�� ���� ������ �� ����
            for k in range(hash_tags_count):
                photos=browser.find_elements_by_css_selector("div._9AhH0")
                photos[k].click()

                browser.implicitly_wait(3)
                try:
                    heart = browser.find_element_by_css_selector('span.fr66n')
                    button= heart.find_element_by_css_selector('button')
                    # html�ڵ忡 ���Ⱑ ���� �� .���� ä���ش�
                    # 'glyphsSpriteHeart__filled__24__red_5 u-__7' ->��glyphsSpriteHeart__filled__24__red_5.u-__7��
                    likebutton= button.find_element_by_css_selector('span.glyphsSpriteHeart__outline__24__grey_9.u-__7')

                    likebutton.click()

                except NoSuchElementException:
                    # NoSuchElementException�� �����ϱ� ���ؼ���
                    # from selenium.common.exceptions import NoSuchElementException�� �ؾ��Ѵ�.
                    print("#"+hash_tags[i]+"�� "+str(k+1)+"��° ������ �̹� ���ƿ䰡 �����ֽ��ϴ�.")


                except IndexError:    
                    print("�� �̻� ������ �����ϴ�.")

                browser.implicitly_wait(2)

                close = browser.find_element_by_xpath("/html/body/div[3]/div/button")
                close.click()

                browser.implicitly_wait(2)

        print('-'*20)
        print('�������ϴ�~')

    def search_by_loc(self,location):
        for i in range(len(location)):
            browser.get('https://www.instagram.com')
            time.sleep(3)
            browser.set_window_size(1024, 600) # �������� ������� Ŀ�� �˻� â�� ���̹Ƿ� ���� ��Ų��.
            time.sleep(2)
            # �ݺ��� �˻�� ���δ�. �̸� �����ϱ� ���� ó���� �˻��� ������ư�� ������ 
            browser.find_element_by_css_selector('div.pbgfb.Di7vw ').click()
            time.sleep(2)
            browser.find_element_by_css_selector('div.aIYm8.coreSpriteSearchClear').click()
            time.sleep(2)
            browser.find_element_by_css_selector("input.XTCLo.x3qfX ").send_keys(location[i])
            time.sleep(2)

            html= browser.page_source
            soup = BeautifulSoup(html,'html.parser')
            page_all = soup.select('a.yCE8d')

            # ��ġ�� �±׷� �˻��ϴ� �Ͱ� �ٸ��� #�� �پ� �����ʴ�. 
            # .text()�� �̿��� tag���� �ؽ�Ʈ�� �������� �װ��� location �� ������
            # href�� �ִ� �ּҸ� �����ٰ� ����.
            url =''

            for page in page_all:
                if page.text == location:
                    url+= page.get('href')
                    print('�˻��� '+location[i]+'��(��) ��ġ�� ��� �Ǿ��ֽ��ϴ�.')
            if url =='':
                print('�˻��� '+ location[i] + '��(��) ��ġ�� ����� �ȵǾ��ֽ��ϴ�.')