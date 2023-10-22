#!/bin/bash
python CapturePhoto.py >/dev/null 2>&1
#sleep 2
python3.9 ParkSense.py &> output.txt
cat output.txt | grep "0:" | cut -d " " -f 3-10 | rev | cut -d "," -f 2-3 | rev
