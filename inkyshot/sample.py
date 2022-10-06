
import time
import os

# lis3dh
import logging
import board
import digitalio
import adafruit_lis3dh
i2c = board.I2C()
int1 = digitalio.DigitalInOut(board.D6)  # Set this to the correct pin for the interrupt!
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)

# Read the preset environment variables and overwrite the default ones
if "DEBUG" in os.environ:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

def main():
    logging.info("I'm okay.")
    while True:
        # update_inkyshot()
        if lis3dh.shake(shake_threshold=10):
            print("Shaken!")
            time.sleep(5)
        elif lis3dh.tapped:
            print("Tapped!")
            time.sleep(0.01)
        print('tapped: ' + str(lis3dh.tapped))
        x, y, z = lis3dh.acceleration
        print(x, y, z)
        delay = 1
        time.sleep(delay)

main()

if __name__ == '__main__':
    main()
# sys.exit(0)
