from pickletools import uint8
import cv2
import numpy as np
import os

def load_image(filePath):
    """

        This function takes in the path of an image as the only parameter 
        and returns a numpy 2D array representing the image.

        Parameters:
            filePath(str): the path to the image, e.g. ex_128.png

        Return:
            image(np array): the image in the form of numpy array 
    """

    if os.path.exists(filePath):
        image = cv2.imread(filePath, 0) # reading an image in grayscale mode
        return image
    else:
        raise FileNotFoundError(f"The path {filePath} is invalid")

def enlarge_image_upper_left(image):
    """
    
    """

    row, col = image.shape
    new_image = np.zeros((row * 2, col * 2), 'uint8')

    for r in range(row):
        for c in range(col):
            new_image[r, c] = image[r, c]

    return new_image

def enlarge_image_interpolation(image):
    """
    
    """
    size = (image.shape[1] * 2, image.shape[0] * 2)
    return cv2.resize(image, size)

def enlarge_image_fill_void(image):
    """
    
    """
    row, col = image.shape
    new_image = np.zeros((row * 2, col * 2), 'uint8')

    for r in range(row):
        for c in range(col):
            new_image[r*2, c*2] = image[r][c]

    return new_image