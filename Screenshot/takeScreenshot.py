import os
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument('--window-size=1200x825')
options.add_argument('--no-sandbox')
options.add_argument('--user-agent="Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0"')
driver = webdriver.Chrome('./chromedriver', options=options)
#url = "https://embed.windy.com/embed2.html?lat=53.514&lon=-2.944&detailLat=53.393&detailLon=-2.134&width=530&height=490&zoom=4&level=surface&overlay=wind&product=ecmw>
url = "http://192.168.178.73:8123/dashboard-test/0"

driver.get(url)
driver.fullscreen_window()
driver.implicitly_wait(1)
#driver.set_window_size(530,445)
driver.save_screenshot('tmp.png')
driver.quit()


Image.open("tmp.png").save("pika.bmp")
os.remove("tmp.png")
