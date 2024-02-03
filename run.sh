#!/bin/bash

path="/home/pi/ePaper"
LOCKFILE="$path/run.sh.lock"
subject="http://192.168.178.73:8123/dashboard-test/0"
api="http://192.168.178.69:3000/api/screenshot?"
url="$apiresX=1200&resY=825&outFormat=png&waitTime=9000&isFullPage=false&dismissModals=true&url=$subject"

if [ -e "$LOCKFILE" ]; then
    exit 1
fi

touch "$LOCKFILE"

curl -o screenshot.png "$url"
convert screenshot.png screenshot.bmp

sudo $path/IT8951 0 0 pika.bmp
rm $path/pika.bmp

rm "$LOCKFILE"
