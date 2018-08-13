
# coding: utf-8

# In[1]:


from selenium import webdriver


# id = input("id을 입력하시오 :") # id,password 입력

# pw = input("pw을 입력하시오 :")

# In[7]:


driver = webdriver.Chrome('C:/Users/Kim/Desktop/chromedriver.exe')


# ## 원하는 지역을 입력 

# In[45]:


Place = input("태그를 입력하시오 :")


# In[9]:


driver.get('https://www.instagram.com/')


# In[10]:


login_link = driver.find_element_by_css_selector('p.izU2O').find_element_by_css_selector('a')


# In[11]:


login_link.click()


# In[12]:


login_button=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/span/button')


# In[20]:


id_input=driver.find_elements_by_css_selector("input._2hvTZ")[0]
pass_input=driver.find_elements_by_css_selector("input._2hvTZ")[1]
id_input.send_keys(id)
pass_input.send_keys(pw)


# In[21]:


login_button.click()


# ### 원하는 지역 url로 접근 => location url이 규칙이 없음
# ### 직접 검색 -> location 아이콘이 있는 것 검색 후 클릭

# ## location url : https://www.instagram.com/explore/locations/~ 
# ### 검색창에서 서울 검색시 지역을 나타내는 아이콘 나옴
# ### 이것을 활용을 할려했지만 못찾는다고 뜸.

# In[56]:


Find_location = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input') 


# In[57]:


Find_location.send_keys(Place)


# In[73]:


Find_locationmark=driver.find_elements_by_css_selector('a.yCE8d  ').find_elements_by_css_selector('div.nebtz coreSpriteLocation')


# In[71]:


Find_locationmark


# In[64]:


Find_locationmark

