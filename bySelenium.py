import re

import requests
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import multiThreadClass

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    # "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
)
# driver = webdriver.Chrome()
driver = webdriver.PhantomJS(desired_capabilities=dcap)
headers = {
    "Accept": "applicatoin/json",
    "Accept-Encoding": "gzip,deflate,sdch,br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    # "Referer":"https://buluo.qq.com/p/detail.html?bid=336575&pid=3981008-1484825285",
    "Prama": "no-cache",
    "Cache-Control": "no-cache"
}

driver.get('https://buluo.qq.com/')
# driver.get('https://qzone.qq.com/')
# driver.find_element_by_xpath("//a[@data-cmd='login']").click()
# driver.find_element_by_class_name("btn-login").click()
# driver.switch_to.frame("login_frame")

# soup = BeautifulSoup(driver.page_source, 'xml')
# index
driver.find_elements_by_xpath("//a[@data-cmd]")[0].click()
driver.switch_to.frame("login_frame")
time.sleep(1)
driver.find_element_by_id("switcher_plogin").click()

driver.find_element_by_id("u").clear()
driver.find_element_by_id("u").send_keys("qq账号：398080994（👀）")
driver.find_element_by_id("p").clear()
driver.find_element_by_id("p").send_keys("qq密码")

driver.find_element_by_class_name("btn").click()
time.sleep(1)
print("completed login and coo")
driver.get("https://buluo.qq.com/p/barindex.html?bid=227061")
# driver.get("https://buluo.qq.com/p/barindex.html?bid=336575")
cookies = driver.get_cookies()
cookieStr = ""
cookieDict = {}
for i in cookies:
    cookieDict[i["name"]] = i["value"]
print(cookieDict)
multiThreadClass.cookieDict = cookieDict
# index = requests.get(url="https://buluo.qq.com/p/index.html",cookies=cookieDict,verify=False,headers=headers)
# totalBuluoRe = re.compile(r"(?<=class=\"name\")")
buluoUrl = "https://buluo.qq.com/p/barindex.html?bid=336575"

searchSecondLayer = multiThreadClass.SearchSecondLayer(buluoUrl)
searchSecondLayer.setDaemon(True)
searchSecondLayer.start()
# commentDict = {
#     "bid":"336575",
#     "pid":"7782215-1489400939",
#     "num":20,
#     "start":0,
#     "barlevel":1
# }
#
# secondLayerContent = requests.get(buluoUrl,cookies=cookieDict,verify=False,headers=headers)
# thirdLayerContentUrlRe = re.compile(r"buluo.qq.com/p/detail.html.*?(?=\")")
# thirdContentUrl = thirdLayerContentUrlRe.findall(secondLayerContent.content.decode())

# for i in thirdContentUrl:
#     i = ("https://" + i).replace("&amp;","&")
#     headers["referer"] = i
#     cur = requests.get(i,cookies= cookieDict,headers = headers,verify= False)
#     commentDict["bid"] = re.compile("(?<=bid=).*(?=&)").findall(i)[0]
#     commentDict["pid"] = re.compile("(?<=pid=).*").findall(i)[0]
#     r = requests.get(url="https://buluo.qq.com/cgi-bin/bar/post/get_comment_by_page_v2",cookies=cookieDict,verify=False,headers=headers,params=commentDict)
#     print()
#
# print(r.content.decode())
# requests.get()

print()
