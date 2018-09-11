"""
Benjamin Shapiro - Homework 7
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

def image_load(filename):
    return plt.imread(filename)


def image_gen(file, steps=30):
    """Generator for image arrays."""
    img1 = image_load(file)     # load file to ndarray
    img2 = convert_bw(img1)
    
    print(img2[0][0])
            
    # go from img1 to img2 than back to img1. s varies from 0 to 1 and then back to 0:
    svalues = np.hstack([np.linspace(0.0, 1.0, steps), np.linspace(1.0, 0, steps)])

    # construct now the list of images, so that we don't have to repeat that later:
    images = [np.uint8(img1 * (1.0 - s) + img2 * s) for s in svalues]    

    # get a  new image as a combination of img1 and img2
    while True:             # repeat all images in a loop
        for img in images:
           yield img 

def convert_bw(img):
    bw = img.copy()
    bw[:] = bw.mean(axis=-1)
    return bw      
    
            
fig = plt.figure()
# create image plot and indicate this is animated. Start with an image.
im = plt.imshow(image_load("florida-keys-800-480.jpg"), interpolation='none', animated=True)

# the two images must have the same shape:
imggen = image_gen("florida-keys-800-480.jpg", steps=30)

# updatefig is called for each frame, each update interval:
def updatefig(*args):
    global imggen
    img_array = next(imggen)     # get next image animation frame
    im.set_array(img_array)       # set it. FuncAnimation will display it
    return (im,)

# create animation object that will call function updatefig every 60 ms
ani = animation.FuncAnimation(fig, updatefig, interval=60, blit=False)
plt.title("Convert to B and W")
plt.show()
