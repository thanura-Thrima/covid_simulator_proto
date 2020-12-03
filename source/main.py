import numpy
import PIL
from PIL import Image, ImageDraw
from app import Application
import time


def main():
    print("---------------  starting  --------------")

    app = Application(1000,"My simmulation")
    time.sleep(5)
    app.run()

if __name__ == "__main__":
    main()


