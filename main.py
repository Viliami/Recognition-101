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

def contains_corner(points,corner):
    p_x1,p_y1 = points[0]
    p_x2,p_y2 = points[2]
    c_x,c_y = corner
    #print("c_x = %i\nc_y = %i\np_x1 = %i\np_y1 = %i\np_x2 = %i\np_y2 = %i"%(c_x,c_y,p_x1,p_y1,p_x2,p_y2))
    if(c_x >= p_x1 and c_x <= p_x2 and c_y >= p_y1 and c_y <= p_y2):
        return True
    return False

def shape_name(corners_amount):
    c = corners_amount
    if(c <= 2):
        return "???"
    elif(c >= 26):
        return "Circle"
    elif c == 3:
        return "Triangle"
    elif c == 4:
        return "Rectangle"
    elif c == 5:
        return "Pentagon"
    elif c == 6:
        return "Hexagon"
    elif c == 7:
        return "Heptagon"
    elif c == 8:
        return "Octagon"
    elif c == 9:
        return "Nonagon"
    elif c == 10:
        return "Decagon"
    elif c == 11:
        return "Hendecagon"
    elif c == 12:
        return "Dodecagon"
    else:
        return str(corners_amount)+"-gon"

for file in files:
    new_img = Image(file)
    plain_img = Image(file)
    new_img = new_img.binarize()
    blobs = new_img.findBlobs()
    corners = new_img.findCorners()

    if(blobs):
        blobs.draw()

    for blob in blobs:
        points = gen_rect_points(blob)
        new_img.dl().polygon(points,filled = True, color=Color.RED)

    if(corners):
        corners.draw()

    print(list(corners[0].coordinates()))
    
    blobs_counter = list()
    for blob in blobs:
        counter = 0
        for corner in corners:
            if(contains_corner(gen_rect_points(blob),corner.coordinates())):
                counter+=1
            #print(contains_corner(gen_rect_points(blobs[1]),corner.coordinates()))
        print(counter)
        #print(contains_corner(gen_rect_points(blobs[1]),corners[1].coordinates()))
        plain_img.drawText(shape_name(counter),blob.minX(),blob.coordinates()[1],(255,0,0))
        blobs_counter.append(counter)

    plain_img.show()
    plain_img.save("images/processed.jpg")
    time.sleep(2)
