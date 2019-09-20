#!/usr/bin/env python
# coding: utf-8

# In[96]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import uuid 
from selenium.common.exceptions import NoSuchElementException 
import requests 
import time


# In[97]:


driver = webdriver.Chrome('/Users/jasonsmellz/Documents/notebooks/chromedriver') #replace with .Firefox(), or with the browser of your choice
# Nike Shoes & Sneakers 
url = "https://store.nike.com/us/en_us/pw/shoes/oi3?cp=usns_us_nike_290519_su19_aw_kw_xcat_serve_fm_x_x_x_x_x_x_x_x_x_nike%20shoes_x_x_x_dfa&gclid=Cj0KCQjw_r3nBRDxARIsAJljleGe1SSQs0oH55oQCSffVyWScQcpHvq2BlMstB3vWg0bnp4uMb_R2JgaAlvIEALw_wcB&gclsrc=aw.ds&ipp=120" 
driver.get(url) #navigate to the page
last_location = 0
last_height = 0 
urls = []
count = 0 


# Meat & Potatoes 

# In[98]:


# scroll to last accessible image  
def scroll_down():

    global last_location 
    global urls 
    
    while True:
        
        # parse images of Nike shoes when made available by scrolling 
        get_images()
        
        print(last_location)
        print(len(urls))
        # Scroll down to the last location.
        driver.execute_script("window.scrollTo(0, {});".format(last_location))

        # Wait to load the page.
        time.sleep(1)


# In[ ]:


def get_images():
    
    global last_height 
    global last_location
    global urls
    global count
    
    current_location = 0 
    
    for element in driver.find_elements_by_class_name('grid-item-image-wrapper'):

        if check_exists(element) :
            
            count += 1
            image_url = element.find_element_by_css_selector("img").get_attribute("src")
            
            # get height of current image in question
            current_location = element.find_element_by_css_selector("img").location["y"]
            
            # save should go function here 
            if current_location > last_location : 
#             print(image_url)
                urls.append(image_url)

#     print('total number of elements with hrefs =', len(urls),'\n', urls, '\n')
    
    # after iterating all available elements - make current_location of last element equal to last_location
    last_location = current_location
    print(urls)


# In[ ]:


def check_exists(element):
    try:
        element.find_element_by_css_selector("img")
    except NoSuchElementException:
        return False
    return True


# In[ ]:


scroll_down()
print(urls)


# In[ ]:




