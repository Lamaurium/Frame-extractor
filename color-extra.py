# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])
boundaries = [
    ([0, 0, 0], [10, 10, 10]),
    ([250, 250, 250], [255, 255, 255])
]

for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    print "a"
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    # show the images
    cv2.imshow("images"+ str((lower, upper)), mask)
cv2.waitKey(0)
