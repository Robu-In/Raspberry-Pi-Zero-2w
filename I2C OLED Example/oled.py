from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from time import sleep
from PIL import ImageFont


def main():
        serial = i2c(port=1, address=0x3c)
        device = ssd1306(serial)

        try:
                font = ImageFont.truetype("arial.tff",16)
        except IOError:
                font = ImageFont.load_default()


        while True:
                with canvas(device) as draw:
                        draw.text((5,5), "Hello World", font=font, fill= 255)
                sleep(1)


if __name__ == "__main__":
        main()