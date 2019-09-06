from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
import random

#前置代码
desires_caps = {}
desires_caps['platformName'] = 'Android'
desires_caps['platformVersion'] = '9'
desires_caps['deviceName'] = '3EP0219129006133'
desires_caps['appPackage'] = 'com.qiyi.video'
desires_caps['appActivity'] = 'org.qiyi.android.video.MainActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desires_caps)

#解决弹窗
def DealThePopWindow():

    try:
        clickprotectprivacy = driver.find_element_by_xpath("//*[@index='2']")
        if clickprotectprivacy:
            clickprotectprivacy.click()
    except:
        pass
    time.sleep(3)

    try:
        clickrightmanagement = driver.find_element_by_xpath("//*[@resource-id='android:id/button1']")
        if clickrightmanagement:
            clickrightmanagement.click()
    except:
        pass

    time.sleep(3)
    try:
        clickIKnow = driver.find_element_by_xpath("//*[@resource-id='com.qiyi.video:id/close']")
        if clickIKnow:
            clickIKnow.click()
    except:
        pass

    time.sleep(3)
    try:
        clickremainmelater = driver.find_element_by_xpath("//*[@index='3']")
        if clickremainmelater:
            clickremainmelater.click()
            print("ok")
    except:
        pass
    time.sleep(3)

class Play():
    """播放视频"""
    def TapToPlay(self):
        TouchAction(driver).tap(x=303, y=1846).perform()
        time.sleep(25)


    def EnlargeWindow(self):
        """窗口最大化(注意这里放大是在播放广告的时候，如果是正在播放视频内容的时候放大应该重新获取一下放大键的元素)"""
        driver.find_element_by_id("com.qiyi.video:id/btn_ads_to_landscape_pre_ad").click()


    def ChangeChannels(self):
        """切台50次这个可能使用时会出错"""
        texts = []
        texts.append(driver.find_elements_by_xpath("//*[@class='android.support.v7.widget.RecyclerView']" and "//*[@index='5']"))
        i = 0
        while i < 50:
            for t in texts:
                print(texts)
                t = random.randint(0,texts)
                m = "//*[@text='t']"
                driver.find_element_by_xpath(m).click()
            i += 1
        time.sleep(80)


    def Dragbar(self):
        """拖动进度条"""
        TouchAction(driver).press(x=330,y=623).move_to(x=410,y=623).move_to(x=621,y=623)
        time.sleep(3)



    def Adjustlight(self):
        """调节亮度"""
        driver.swipe(start_x=276,start_y=574,end_x=226,end_y=113,duration=1)
        time.sleep(3)







