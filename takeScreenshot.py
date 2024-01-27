import os
import time
from PIL import Image
from dotenv import load_dotenv
from selenium import webdriver
from multiprocessing import Process
from selenium.webdriver.chrome.options import Options

load_dotenv()

hostname = os.getenv('HOSTNAME')
url = os.getenv('URL')
path = os.getenv('PATH')

def screenshot():
    # Browser options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    
    # Add path to the PATH environment variable
    os.environ["PATH"] += os.pathsep + '/usr/bin/chromedriver'
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    driver.execute_script("document.body.style.zoom='250%'") # 
    driver.save_screenshot('tmp.png')
    driver.quit()

    # converts .jpg to .bmp
    Image.open("tmp.png").save("pika.bmp")
    os.remove("tmp.png")

    quit()

if __name__ == '__main__':

    # checks if the webserver is online
    #response = os.system("ping -c 1 " + hostname)
    response = 0

    if response == 0:
        # Start screenshot as a process
        p = Process(target=screenshot)
        p.start()
        p.join(timeout=20)
        p.terminate()
    else:
        quit()