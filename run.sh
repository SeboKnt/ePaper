#!/bin/bash

path="/home/pi/ePaper"

sudo python3 $path/takeScreenshot.py
sudo $path/IT8951 0 0 pika.bmp
sudo rm $path/pika.bmp
