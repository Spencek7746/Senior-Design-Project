#!/bin/bash
#sleep 2
#python CapturePhoto.py "$1" >/dev/null 2>&1
libcamera-still -n --immediate -v 0 -o "img/unprocessed$1.jpg"
#sleep 2
python3.9 ParkSense.py "$1" &> output.txt
cat output.txt | grep "0:" | cut -d " " -f 3-10 | rev | cut -d "," -f 2-3 | rev
