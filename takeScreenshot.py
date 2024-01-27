import os
import time
from PIL import Image
from dotenv import load_dotenv
from selenium import webdriver
from multiprocessing import Process
from selenium.webdriver.firefox.options import Options

load_dotenv()

hostname = os.getenv('HOSTNAME')
url = os.getenv('URL')

def screenshot():
    # Browser options
    options = Options()
    options.add_argument("--headless")
    
    # Add path to the PATH environment variable
    driver = webdriver.Firefox(options=options)

    driver.get(url)
    driver.execute_script("document.body.style.zoom='250%'") # 
    driver.save_screenshot('tmp.png')
    driver.quit()

    # converts .png to .bmp
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