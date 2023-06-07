from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import yaml
import re

class ChromeDriver(webdriver.Chrome):
    def __init__(self,chrome_options,executable_path='chromedriver'):
        super(ChromeDriver,self).__init__(chrome_options=chrome_options,
                                          executable_path=executable_path)
        
    def load_url(self,url,wait=5):
        self.get(url)
        time.sleep(wait)

    def require_login(self,
                      username=None,
                      password=None,
                      css_selector_username="input[type='text']",
                      css_selector_password="input[type='password']",
                      css_selector_submit="input[type='submit']",
                      wait=5):
        
        if username=='' or password=='':
            config=yaml.safe_load(open('./config/config.yaml'))
            username=config['username']
            password=config['password']
            
        self.find_element(By.CSS_SELECTOR, css_selector_username).send_keys(username)
        self.find_element(By.CSS_SELECTOR, css_selector_password).send_keys(password)
        self.find_element(By.CSS_SELECTOR, css_selector_submit).click()
        time.sleep(wait)

    def anime_picture_crawl_from_post_id(self,post_id,wait=1):
        self.load_url(f'https://danbooru.donmai.us/posts/{str(post_id)}',wait=wait)
        character_tags=[]
        general_tags=[]
        copyright_tags=[]
        image_url=''
        datetime=''
        artist_tags=[]
        meta_tags=[]
        
        img=self.find_element(By.CSS_SELECTOR,"section[class='image-container note-container blacklisted']")
        image_url=img.get_attribute('data-file-url')
        date=self.find_element(By.CSS_SELECTOR,"li[id='post-info-date']").find_element(By.TAG_NAME,'a').find_element(By.TAG_NAME,'time')
        datetime=date.get_attribute('datetime')
        tags=self.find_element(By.CSS_SELECTOR,"div[class='tag-list categorized-tag-list']")
        try:
            _general_tags=tags.find_elements(By.CSS_SELECTOR,"li[class='tag-type-0']")
            for el in _general_tags:
                el=el.find_element(By.CSS_SELECTOR,"a[class='search-tag']")
                general_tags.append(el.text)

            _character_tags=tags.find_elements(By.CSS_SELECTOR,"li[class='tag-type-4']")
            for el in _character_tags:
                el=el.find_element(By.CSS_SELECTOR,"a[class='search-tag']")
                character_tags.append(el.text)

            _artist_tags=tags.find_elements(By.CSS_SELECTOR,"li[class='tag-type-1']")
            for el in _artist_tags:
                el=el.find_element(By.CSS_SELECTOR,"a[class='search-tag']")
                artist_tags.append(el.text)
            
            _copyright_tags=tags.find_elements(By.CSS_SELECTOR,"li[class='tag-type-3']")
            for el in _copyright_tags:
                el=el.find_element(By.CSS_SELECTOR,"a[class='search-tag']")
                copyright_tags.append(el.text)

            _meta_tags=tags.find_elements(By.CSS_SELECTOR,"li[class='tag-type-5']")
            for el in _meta_tags:
                el=el.find_element(By.CSS_SELECTOR,"a[class='search-tag']")
                meta_tags.append(el.text)

        except:pass

        return {
            'id':post_id,
            'character_tags':character_tags,
            'general_tags':general_tags,
            'meta_tags':meta_tags,
            'image_url':image_url,
            'artist_tags':artist_tags,
            'copyright_tags':copyright_tags,
            'datetime':datetime
        }
