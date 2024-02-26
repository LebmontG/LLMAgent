'''
Crawler for https://zbtb.caac.gov.cn/sub-page/index/zbggList.html
ZGan 2024.1.23
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import lxml
from bs4 import BeautifulSoup
import time
import os

url = 'https://zbtb.caac.gov.cn/sub-page/index/zbggList.html'
index="空管"
pagenum=57
path="XJ/"
if not os.path.exists(path):os.mkdir(path)

driver = webdriver.Firefox()
driver.get(url)
time.sleep(4)

search=driver.find_element(By.ID,'projName')
search.send_keys(index)
sch_btn=driver.find_element(By.ID,'search')
sch_btn.click()
time.sleep(1)

text=[]
while pagenum:
    table = driver.find_element(By.ID,'dataTable')
    rows = table.find_elements("tag name",'tr')
    
    for row in rows:
        i=row.get_attribute('id')
        if not i:continue
        driver.find_element("xpath",f'//*[@id="{i}"]').click()
        time.sleep(1.5)
        driver.switch_to.window(driver.window_handles[-1])
        
        frame=driver.find_elements('tag name',"iframe")
        if len(frame):driver.switch_to.frame(frame[0])
        t = driver.find_elements("tag name",'p')
        # tmp=""
        if len(t):
            if "/" in t[0].text or "\\" in t[0].text:
                name=t[0].text.split("/")[0].split("\\")[0]
            else:name=t[0].text
            # name=name.encode("gbk",errors="ignore").decode("gbk")
            f=open(path+name+".txt","w",encoding='utf-8')
            for l in t:
                f.write(l.text+"\n")
            f.close()
        # text.append(tmp)
        driver.switch_to.default_content()
        
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(0.5)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    btn = driver.find_element(By.ID,'dataTable_next')
    driver.execute_script("arguments[0].click();",btn)
    time.sleep(2)

    pagenum-=1

# url='https://zbtb.caac.gov.cn/sys-content/initPage.html?url=zbgg_init&id=402883448d2028c6018d213529a10601'
# driver = webdriver.Firefox()
# driver.get(url)
# driver.switch_to.frame(driver.find_elements('tag name',"iframe")[0])
# t = driver.find_elements("tag name",'p')
# tmp=""
# for l in t:
#     tmp+=l.text

# import requests
# import json
# # import dryscrape
# from bs4 import BeautifulSoup

# url = 'https://zbtb.caac.gov.cn/sub-page/index/zbggList.html'
# headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}  

# response = requests.get(url, headers=headers)

# data=response.json()

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     for link in soup.find_all('a'):
#         print(link.get('href'))
# else:
#     print(f"Error: {response.status_code}")