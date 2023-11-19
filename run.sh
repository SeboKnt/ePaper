#!/bin/bash

path="/home/pi/ePaper"
LOCKFILE="$path/run.sh.lock"

if [ -e "$LOCKFILE" ]; then
    exit 1
fi

touch "$LOCKFILE"

sudo python3 $path/takeScreenshot.py
sudo $path/IT8951 0 0 pika.bmp
sudo rm $path/pika.bmp

rm "$LOCKFILE"
