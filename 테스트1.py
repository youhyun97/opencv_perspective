# 0416.py
import cv2
import numpy as np
src = cv2.imread('./imgp1.png')

rows, cols, channels = src.shape

#perspective
src_pts = np.float32([[0,0], [0,rows-1], [cols/2,0], [cols/2,rows-1]])
dst_pts = np.float32([[0,50], [0,rows-51], [cols/2,0], [cols/2,rows-1]])

p1=cv2.getPerspectiveTransform(src_pts, dst_pts)
img_sym = cv2.warpPerspective( src, p1, (cols, rows))

#cv2.imshow('dst1',  dst1)
cv2.imshow('dst1', src)
cv2.imshow('dst3',  img_sym)
cv2.waitKey()    
cv2.destroyAllWindows()
