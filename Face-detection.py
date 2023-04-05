import cv2 as cv

img = cv.imread('cc.jpg')

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()