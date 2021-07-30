# First install cv2 into your terminal
# (copy paste this line in your terminal for installing cv2)
# pip install opencv-python

import cv2

# captian.jpg = file name (which you want to convert into sketch)

image = cv2.imread("captian.jpg")

grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

invert = cv2.bitwise_not(grey_img)

blur = cv2.GaussianBlur(invert, (21, 21,), 0)

invertedblur = cv2.bitwise_not(blur)

# adjust scale as per you requirement

sketch = cv2.divide(grey_img, invertedblur, scale=100.0)

# sketch.png = file name(after converting into sketch)

cv2.imwrite("sketch.png", sketch)
