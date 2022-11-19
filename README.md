# ePaper

```
sudo crontab -l
*/2 * * * * /home/pi/ePaper/Screen/IT8951 0 0 /home/pi/ePaper/Screen/pika.bmp

crontab -l 
*/2 * * * * bash /home/pi/ePaper/run.sh >/dev/null 2>&1
```
