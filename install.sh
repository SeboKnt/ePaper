#!/bin/bash

# For screenshot
sudo apt update && sudo apt upgrade -y
sudo apt install chromium-browser
sudo apt-get install libopenjp2-7

pip3 install selenium

sudo apt-get install automake

# Install C++ SPI library for Raspberry
cd bcm2835*
chmod +x configure
./configure
make
sudo make check
sudo make install

# Install 9.7" E-Paper drivers
cd ..
cd IT8951
make clean
make

# Show image
sudo ./IT8951 0 0 pika.bmp
