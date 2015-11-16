import os, glob, time, numpy
from SimpleCV import *

my_images_path = "/home/ubuntu/Documents/Recognition-101/images/"
extension = "*.png"

if not my_images_path:
    path = os.getcwd()
else:
    path = my_images_path

imgs = list()
directory = os.path.join(path, extension)
files = glob.glob(directory)

def gen_rect_points(blob):
    return [(blob.minX(),blob.minY()),(blob.minX(),blob.maxY()),(blob.maxX(),blob.maxY()),(blob.maxX(),blob.minY())]

for file in files:
    new_img = Image(file)
    new_img = new_img.binarize()
    blobs = new_img.findBlobs()
    #edges = new_img.findCorners()
    print("Height",blobs.height())
    print("MaxX = ",blobs[0].maxX())
    print("MaxY = ",blobs[0].maxY())
    if(blobs):
        blobs.draw()
    #if(bottom_edge):
    #    bottom_edge.draw()
    #if(edges):
    #    edges.draw()
    points = gen_rect_points(blobs[0])
    new_img.dl().polygon(points,filled = True, color=Color.RED)
    new_img.show()
    new_img.save("images/processed.jpg")
    #print("Area:",blobs.area())
    #print("Angles:",blobs.angle())
    print("Centers:",blobs.coordinates())
    time.sleep(2)