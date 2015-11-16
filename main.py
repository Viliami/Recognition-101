import os, glob, time
from SimpleCV import *

my_images_path = "/home/ubuntu/Documents/images/"
extension = "*.png"

if not my_images_path:
    path = os.getcwd()
else:
    path = my_images_path

imgs = list()
directory = os.path.join(path, extension)
files = glob.glob(directory)

for file in files:
    new_img = Image(file)
    new_img.show()
    time.sleep(1)
