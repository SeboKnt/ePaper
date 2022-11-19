#!/bin/bash

cd /home/pi/ePaper/Screenshot
python3 ./takeScreenshot.py
mv pika.bmp ../Screen/
cd ../Screen
#  Show image
sudo ./IT8951 0 0 pika.bmp
