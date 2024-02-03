
# ePaper

***a big thx to [@aceisace]( https://github.com/aceisace/Inkycal) for doing all the work***

This project takes a first gen Raspberry Pi Zero WH and the Waveshare [E-ink](https://www.berrybase.de/9.7-1200x825-epaper-display-hat-fuer-raspberry-pi) display 9.7" and builds a dirty way to display browser content on the E-ink screen. The web page to be called and screenshotted can be customized in `takeScreenshot.py`.

# Installation

## Screenshot Script
```
sudo apt update && sudo apt upgrade -y
sudo apt install imagemagick
```

## Screen

### Unzip
```
cd driver
unzip IT8951.zip
unzip bcm2835-1.68.zip
```

### Install C++ SPI library for Raspberry
```
cd bcm2835-1.68
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

### Show example image
`sudo ./driver/IT8951 0 0 pika.bmp`

## CronJob
```
sudo crontab -l
*/5 * * * * /bin/bash /home/pi/ePaper/run.sh >/dev/null 2>&1
```
