# ePaper

```
sudo crontab -l
*/2 * * * * /home/pi/ePaper/Screen/IT8951 0 0 /home/pi/ePaper/Screen/pika.bmp

```


# Instalation

## For Screenshot
sudo apt update && sudo apt upgrade -y
(sudo apt install chromium-browser)
sudo apt-get install libopenjp2-7
sudo apt-get install automake
pip3 install selenium

## For Screen
### Unzip
cd driver
unzip *

### Install C++ SPI library for Raspberry
cd bcm2835*
chmod +x configure
./configure
make
sudo make check
sudo make install

### Install 9.7" E-Paper drivers
cd ..
cd IT8951
make clean
make

### Show image
sudo ./IT8951 0 0 pika.bmp
