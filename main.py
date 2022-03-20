import image
import cv2
import utils
from matplotlib import pyplot as plt
import numpy as np

image_path = "ex_128.png"
# image_path = "the-beatles.jpg"

img = image.load_image(image_path)

# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

dft_result = utils.DFT(img)
dft_magnitude = utils.to_magnitude(dft_result)

fig = plt.figure(figsize=(7,7))
ax1 = fig.add_subplot(2,1,1)
ax1.imshow(img)
ax1.title.set_text('Original')
ax2 = fig.add_subplot(2,1,2)
ax2.imshow(dft_magnitude, cmap='gray')
ax2.title.set_text('Original DFT')
plt.axis('off')
plt.show()

img2 = image.enlarge_image_upper_left(img)

# cv2.imshow("img", img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img3 = image.enlarge_image_interpolation(img)

# cv2.imshow("img", img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img4 = image.enlarge_image_fill_void(img)

# cv2.imshow("img", img4)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
