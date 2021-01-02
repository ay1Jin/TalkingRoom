#__author:ayjin
#__Date:2020-12-29
#__Orginazation:JLUZH
#__Topic:
from selenium import webdriver
import time
url = 'http://wlkc.jluzh.edu.cn/meol/index.do'
chrome = webdriver.Chrome()
chrome.get(url)
chrome.find_element_by_xpath("//div[@class='register login_button']").click()
time.sleep(0.5)
chrome.find_element_by_xpath("//input[@id='userName']").send_keys('06180204')
chrome.find_element_by_xpath("//input[@id='passWord']").send_keys('ouyang4283658')
time.sleep(0.5)
chrome.find_element_by_xpath("//input[@class='submit']").click()
time.sleep(3)
reminder = chrome.find_elements_by_xpath("//div[@class='reminderwrap']//ul[@id='reminder']/li")
# print(len(reminder))
userinfo = chrome.find_elements_by_xpath("//div[@class='userinfobody']//li")
for s in userinfo:
    if len(s.text) != 0:
        print(s.text)
msg = {}
for lis in reminder:
    try:
        title = lis.find_element_by_xpath(".//a")
        # print(title.text)
        title.click()
        time.sleep(0.5)
        names = lis.find_elements_by_xpath(".//ul[@style='display: block;']//li/a")
        content = []
        for name in names:
            # print(name.text)
            content.append(name.text)
        msg[title.text] = content
    except Exception as e:
        print(e)
print(msg)
