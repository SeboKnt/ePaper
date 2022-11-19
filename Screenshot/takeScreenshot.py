import os
import time
import datetime
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

# chrome options
OPTIONS = Options()
OPTIONS.add_argument('--headless')
OPTIONS.add_argument('--window-size=1200x825')
OPTIONS.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36')

url = "http://192.168.178.73:8123/dashboard-test/"
zoom = 200

browser = webdriver.Chrome(executable_path="./chromedriver", options=OPTIONS)
browser.get("http://192.168.178.73:8123/dashboard-test/0")
time.sleep(60)
browser.execute_script("document.body.style.zoom='250%'")
time.sleep(10)
browser.get_screenshot_as_file("tmp.png")
browser.quit()

Image.open("tmp.png").save("pika.bmp")
