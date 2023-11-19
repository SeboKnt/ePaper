import os
import time
from PIL import Image
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "http://192.168.178.73:8123/dashboard-test/0"

def screenshot():
    # Browser options
    options = Options()
    options.headless = True
    options.add_argument('--window-size=1200x825')
    options.add_argument('--no-sandbox')
    options.add_argument('--user-agent="Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0"')
    driver = webdriver.Chrome(f'chromedriver', options=options)

    driver.get(url)
    #time.sleep(80) # Time for the Ri to cope with the situation
    driver.execute_script("document.body.style.zoom='250%'") # 
    driver.save_screenshot('tmp.png')
    driver.quit()

    # converts .jpg to .bmp
    Image.open("tmp.png").save("pika.bmp")
    os.remove("tmp.png")

    quit()


if __name__ == '__main__':

    # checks if the webserver is online
    hostname = "192.168.178.73"
    #response = os.system("ping -c 1 " + hostname)
    response = 0

    if response == 0:
        # Start screenshot as a process
        p = Process(target=screenshot)
        p.start()
        p.join(timeout=180)
        p.terminate()
    else:
        quit()
