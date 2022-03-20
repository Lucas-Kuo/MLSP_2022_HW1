import numpy as np
from matplotlib import pyplot as plt
import cv2

def DFT(image):
    """
    
    """
    row, col = image.shape

    dft_result = np.empty((row, col), complex)

    # for k in range(row):
    #     for l in range(col):
    #         sum = 0
    #         for m in range(row):
    #             for n in range(col):
    #                 sum += image[m, n] * np.exp(-np.pi*2j*(k*m/row + l*n/col))
    #         dft_result[k, l] = sum
    K = int(row/2)
    L = int(col/2)
    for k in range(-K, K):
        for l in range(-L, L):
            sum = 0
            for m in range(row):
                for n in range(col):
                    sum += image[m, n] * np.exp(-np.pi*2j*(k*m/row + l*n/col))
            dft_result[k+K, l+L] = sum
    
    dft_result = dft_result / (row*col)

    return dft_result

    # return np.fft.fftshift(cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT))

def to_magnitude(dft_result):
    """
    
    """
    return 2000 * np.log(np.abs(dft_result))