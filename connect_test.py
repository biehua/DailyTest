__author__ = 'terry'
from selenium import webdriver
from time import sleep

#打开浏览器，建立与浏览器的会话
driver = webdriver.Chrome()
#窗口全屏操作
driver.maximize_window()
#设置屏幕大小
# driver.set_window_size()


#访问网址
driver.get("https://www.baidu.com/")
sleep(2)
driver.get("https://www.taobao.com/")

print(driver.title)
print(driver.current_url)

#返回上一个页面
driver.back()
sleep(2)
#下一个页面
driver.forward()
sleep(2)
#刷新
driver.refresh()

#关闭当前页面的窗口
# driver.close()

#关闭浏览器的会话
driver.quit()