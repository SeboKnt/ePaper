#!/bin/bash

path="/home/pi/ePaper"
LOCKFILE="$path/run.sh.lock"
subject="http://192.168.178.73:8123/dashboard-test/0"
api="http://192.168.178.69:3000/api/screenshot?"
url="${api}resX=300&resY=206&outFormat=png&waitTime=14000&isFullPage=false&dismissModals=true&url=$subject"
kuma="http://192.168.178.69:3001/api/push/1q4lhpcbhN?status=up&msg=OK&ping="

if [ -e "$LOCKFILE" ]; then
    exit 1
fi

touch "$LOCKFILE"

curl -o $path/screenshot.png "$url"
#convert $path/screenshot.png -resize 400% $path/screenshot.png
convert $path/screenshot.png $path/pika.bmp

sudo $path/driver/IT8951/IT8951 0 0 $path/pika.bmp
rm $path/screenshot.png
rm $path/pika.bmp

curl $kuma

rm "$LOCKFILE"
