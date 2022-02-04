import numpy as np
import imageio
import image
import scipy.ndimage
import cv2

# the image to be converted to a sketch

img = "ducati.jpg"


def rgb2gray(rgb):
    # 2D array formula to convert image to grayscale
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])

def dodge(front, back):
    final_sketch = front*255/(255-back)
    # for images greater than 255 revert them to 255
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255

    # to convert any suitable existing column to categorical type, we will use aspect function
    # and uint8 is for 8-bit signed integer
    return final_sketch.astype('uint8')

# to read the given image(img)
s = imageio.imread(img)

# make the image gray scale
gray = rgb2gray(s)

i = 255-gray

# to convert the image into blur
# sigma is the intensity of blurness of image
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)

# to convert the image to sketch by taking in blur and gray as parameters
r = dodge(blur, gray)

cv2.imwrite('ducati-sketch.png', r)
