
# coding: utf-8

# In[120]:


driver.quit()


# ## selenium을 이용한다.

# In[121]:


from selenium import webdriver


# ### id,password입력

# In[ ]:


id = input("id을 입력하시오 :") # id,password 입력


# In[ ]:


pw = input("pw을 입력하시오 :")


# In[124]:


driver = webdriver.Chrome('/chromdriver.exe')


# ### 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.

# In[125]:


driver.implicitly_wait(3)


# ### url 접근

# In[126]:


driver.get('https://www.instagram.com/')


# ### 로그인 접근

# In[127]:


login_link = driver.find_element_by_css_selector('p.izU2O').find_element_by_css_selector('a')


# In[128]:


login_link.click()


# In[135]:


## ID,PW입력 후 로그인 버튼 누르기


# In[129]:


id_input=driver.find_elements_by_css_selector("input._2hvTZ")[0]


# In[130]:


id_input.send_keys(id)


# In[131]:


pass_input=driver.find_elements_by_css_selector("input._2hvTZ")[1]


# In[132]:


pass_input.send_keys(pw)


# In[133]:


driver.find_element_by_css_selector('button._5f5mN').click()


# In[ ]:


#span.glglyphsSpriteHeart__outline__24__grey_9 u-__7 =>빈리스트로 나와서 
#span -> button으로 바꿨다.


# In[134]:


for i in range(5):
    Button_like=driver.find_elements_by_css_selector('span.fr66n')[i].find_element_by_css_selector('button')
    Button_like.click()

