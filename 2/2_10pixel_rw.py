# -*- coding: utf-8 -*-
import cv2

img = cv2.imread("../image/1_1.jpg")
(b, g, r) = img[100, 100]
print(b, g, r)

for i in range(1, 100):
    img[10 + i, 100] = (255, 0, 0)
cv2.imshow('image', img)
cv2.waitKey(0)