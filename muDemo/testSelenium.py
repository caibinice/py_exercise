from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 使用谷歌浏览器的headless模式（无界面的后台）访问url，一般用于爬虫
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.baidu.com")
# 获取网页dom元素进行操作
driver.find_element(by="id", value='kw').send_keys('搜索')
driver.find_element(by="id", value='su').click()

time.sleep(2)
# 截图看效果
driver.save_screenshot('./ch.png')

driver.quit()

