import time
import sys

from picamera2 import Picamera2, Preview

outputPath = "./img/"

if __name__ == "__main__":
  if len(sys.argv) > 1:
    outputPath += "unprocessed" + str(sys.argv[1]) + ".jpg"
  else:
    outputPath += "unprocessed.jpg"
  print(outputPath)
  picam2 = Picamera2()
#640 x 480
  camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (1920, 1080)}, display="lores")
  picam2.configure(camera_config)
  picam2.start()
  picam2.capture_file(outputPath)

