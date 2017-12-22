import hashlib
import re
import threading
from datetime import datetime

import requests
import time
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver

cookieDict = {}
verify = False
itemsDict = {}
threadsPool = []
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


class Item():
    uin = ""
    content = ""


isNewThread = True


class ThreadsMonitor(threading.Thread):
    def __init__(self, size):
        threading.Thread.__init__(self)
        self.stop = False
        self.size = size
        self.count = 0

    def run(self):
        global isNewThread
        while (self.stop == False):
            count = 0
            for i in threadsPool:
                if (i.isAlive() == False):
                    threadsPool.remove(i)
                else:
                    count += 1
            self.count = count
            isNewThread = self.isNewThread()

    def isNewThread(self):
        if (self.count < self.size):
            return True
        else:
            return False

    def stop(self):
        self.stop = True


class SearchThirdLayer(threading.Thread):
    def __init__(self, url, contentLimit=10):
        threading.Thread.__init__(self)
        self.stop = False
        self.url = url
        # self.commentsUrl = "https://buluo.qq.com/cgi-bin/bar/post/get_comment_by_page_v2?" + re.compile("bid=.*(?=&)").findall(self.url) + "&" + re.compile("pid=.*(?=&)").findall(self.url)
        self.commentsUrl = "https://buluo.qq.com/cgi-bin/bar/post/get_comment_by_page_v2"
        self.contentLimit = contentLimit
        self.headers = headers
        self.headers["Referer"] = self.url
        self.params = {"bid": re.compile("(?<=bid=).*(?=&)").findall(self.url)[0],
                       "pid": re.compile("(?<=pid=).*").findall(self.url)[0],
                       "num": 20,
                       "start": 0,
                       "barlevel": 1
                       }

    def run(self):
        if (self.stop == False):
            thirdLayerContent = requests.get(url=self.commentsUrl, cookies=cookieDict, headers=self.headers,
                                             params=self.params, verify=False)

            thirdLayerContentRe = re.compile(r"(?<=\"uin\":).*?(?=,)")
            thirdLayerUinRe = re.compile(r"(?<=\"uin\":).*?(?=,)")

            # r = requests.get(self.commentsUrl,cookies= cookieDict, headers = self.headers, params=self.params,verify = False)
            # contents = thirdLayerContentRe.findall(thirdLayerContent.content.decode())
            uins = thirdLayerUinRe.findall(thirdLayerContent.content)
            # TODO add limitation
            for uin in uins:
                itemsDict[uin] = 1
                print("add qq", uin)
                if (self.stop):
                    return;

    def stop(self):
        self.top = True


class SearchSecondLayer(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.stop = False

    def run(self):
        if (self.stop == False):
            secondLayerContent = requests.get(url=self.url, cookies=cookieDict, verify=False)
            thirdLayerUrlRe = re.compile(r"buluo.qq.com/p/detail.html.*?(?=\")")
            totalThirdLayerUrl = thirdLayerUrlRe.findall(secondLayerContent.content)
            # TODO add limitation
            for i in totalThirdLayerUrl:
                curThread = SearchThirdLayer(("https://" + i).replace("&amp;", "&"))
                curThread.setDaemon(True)
                curThread.start()
                time.sleep(5)

    def stop(self):
        self.stop = True


# class SearchFirstLayer(threading.Thread):
#     def __init__(self,url):
#         threading.Thread.__init__()
#         self.url = url
#     def run(self):
#
class connectRuokuai():
    def __init__(self, uin, pwd):
        self.id = "77368"
        self.key = "0d830378d07e47fa9507636fc1dab95f"
        self.un = uin
        self.pwd = pwd
        # 2040为4位纯字母
        self.typeid = "2040"
        self.url = "http://api.ruokuai.com/create.xml"
        self.headers = {
            "Accept": "* / *",
            "Accept - Language": "zh - cn",
            "Content - Type": "multipart / form - data",
            "boundary": "-------------RK",
            "Host": "api.ruokuai.com"
        }
        pass

    # def http_request(self, url, paramDict):
    #     post_content = ''
    #     for key in paramDict:
    #         post_content = post_content + '%s=%s&'%(key,paramDict[key])
    #     post_content = post_content[0:-1]
    #     #print post_content
    #     req = urllib2.Request(url, data=post_content)
    #     req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    #     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    #     response = opener.open(req, post_content)
    #     return response.read()
    def http_upload_image(self, url, paramKeys, paramDict, filebytes):
        timestr = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        boundary = '------------' + hashlib.md5(timestr.encode()).hexdigest().lower()
        boundarystr = '\r\n--%s\r\n' % (boundary)

        bs = b''
        for key in paramKeys:
            bs = bs + boundarystr.encode('ascii')
            param = "Content-Disposition: form-data; name=\"%s\"\r\n\r\n%s" % (key, paramDict[key])
            # print param
            bs = bs + param.encode('utf8')
        bs = bs + boundarystr.encode('ascii')

        header = 'Content-Disposition: form-data; name=\"image\"; filename=\"%s\"\r\nContent-Type: image/gif\r\n\r\n' % (
            'sample')
        bs = bs + header.encode('utf8')

        bs = bs + filebytes
        tailer = '\r\n--%s--\r\n' % (boundary)
        bs = bs + tailer.encode('ascii')

        import requests
        headers = {'Content-Type': 'multipart/form-data; boundary=%s' % boundary,
                   'Connection': 'Keep-Alive',
                   'Expect': '100-continue',
                   }
        response = requests.post(url, params='', data=bs, headers=headers)
        return response.text

    def postData(self, imageurl):
        params = {
            "username": self.un,
            "password": self.pwd,
            "typeid": self.typeid,
            "timeout": 60,
            "softid": self.id,
            "softkey": self.key,
            "imageurl": imageurl

        }
        paramKeys = ['username',
                     'password',
                     'typeid',
                     'timeout',
                     'softid',
                     'softkey'
                     ]
        # r = requests.post(url=self.url, data=params,verify=False)

        filebytes = requests.get(imageurl).content
        result = self.http_upload_image("http://api.ruokuai.com/create.xml", paramKeys, params, filebytes)
        verifycode = re.compile(r"(?<=Result>).*?(?=<)").findall(result)[0]
        return verifycode


class Login():
    loginUrl = ""

    def __init__(self, uin, pwd):
        self.uin = uin
        self.pwd = pwd

    def mockBySelenium(self):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            # "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        )
        driver = webdriver.Chrome()
        # driver = webdriver.PhantomJS(desired_capabilities=dcap)
        driver.get('https://buluo.qq.com/')
        driver.find_elements_by_xpath("//a[@data-cmd]")[0].click()
        driver.switch_to.frame("login_frame")
        time.sleep(1)
        driver.find_element_by_id("switcher_plogin").click()

        driver.find_element_by_id("u").clear()
        driver.find_element_by_id("u").send_keys(self.uin)
        driver.find_element_by_id("p").clear()
        driver.find_element_by_id("p").send_keys(self.pwd)

        driver.find_element_by_class_name("btn").click()
        time.sleep(1)
        try:
            driver.switch_to.frame(0)
            driver.find_element_by_id("capImg")
            verifycodeUrl = driver.find_elements_by_xpath("//img[@src]")[0].get_attribute("src")
            ruokuai = connectRuokuai("xiaochaohcoa", "123456789qwer")
            verifycode = ruokuai.postData(verifycodeUrl)
            driver.find_element_by_id("capAns").clear()
            driver.find_element_by_id("capAns").send_keys(verifycode)
            driver.find_elements_by_id("submit")[0].click()
        except:
            print("no need for vc")
        time.sleep(1)
        print("completed login and coo")
        driver.get("https://buluo.qq.com/p/barindex.html?bid=227061")
        cookies = driver.get_cookies()
        for i in cookies:
            cookieDict[i["name"]] = i["value"]
        self.cookieDict = cookieDict
        print(cookieDict)
        return cookieDict


class Main():
    def __init__(self, uin, pwd):
        self.uin = uin
        self.pwd = pwd

    def main(self):
        curLogin = Login(self.uin, self.pwd)
        cookie = curLogin.mockBySelenium()
        print(cookie)


m = Main("脱敏", "脱敏")
m.main()
