from github import Github
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

username = "**************"
password = "**************"

class Github:
    def __init__(self , username , password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
        
    def sigIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(3)
        
        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)
        time.sleep(2)
        
        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]").click()
     
    def loadFollowers(self):
        items = self.browser.find_elements_by_css_selector("position-relative")
                    
        for i in items:
            n = self.followers.append(i.find_elements(".f4.Link--primary"))
            ementa = getattr(n, 'text')
    
    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)
        
        self.loadFollowers()
            
        while True:
            links = self.browser.find_element_by_class_name("paginate-container").find_elements_by_tag_name("a")
            
            if len(links) == 1:
                if len[0].text == "Next":
                    links[0].click()
                    time.sleep(1)
                    
                    self.loadFollowers()
                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(2)
                        
                        self.loadFollowers()
                    else:
                        continue
github = Github(username , password)
github.sigIn()
github.getFollowers()
print(len(github.followers))
print(github.followers)