
# ePaper

***a big thx to [@aceisace]( https://github.com/aceisace/Inkycal) for doing all the work***

This project takes a first gen Raspberry Pi Zero WH and the Waveshare [E-ink](https://www.berrybase.de/9.7-1200x825-epaper-display-hat-fuer-raspberry-pi) display 9.7" and builds a dirty way to display browser content on the E-ink screen. The web page to be called and screenshotted can be customized in `takeScreenshot.py`.

# Installation

## Screenshot
```
sudo apt update && sudo apt upgrade -y
# sudo apt install chromium-browser
sudo apt-get install libopenjp2-7
sudo apt-get install automake
pip3 install selenium
pip3 install python-dotenv
```

## Screen

### Unzip
```
cd driver
unzip *
```

### Install C++ SPI library for Raspberry
```
cd bcm2835*
chmod +x configure
./configure
make
sudo make check
sudo make install
```

### Install 9.7" E-Paper drivers
```
cd ..
cd IT8951
make clean
make
```

### Show image
`sudo ./IT8951 0 0 pika.bmp`

## CronJob
```
sudo crontab -l
*/5 * * * * /home/pi/ePaper/Screen/IT8951 0 0 /home/pi/ePaper/Screen/pika.bmp >/dev/null 2>&1
```
