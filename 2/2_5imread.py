# -*- coding: utf-8 -*-

import tensorflow as tf
import cv2

# 0 gray 1 color
img = cv2.imread('../image/1.jpg', 1)
cv2.imshow('image', img)
cv2.waitKey(0)