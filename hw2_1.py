import cv2
import numpy as np

imageFile = './a4.jpg'
src3 = cv2.imread('./duksung_symbol2.png') #덕성 로고
img = cv2.imread(imageFile) #color로 imageFile 읽기
dst = cv2.resize(img, dsize=(600, 600)) # img (600,600) 크기로 조절

a = []
def onMouse(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽 마우스 클릭시
    cv2.circle(param[0], (x, y), 8, (255,0,0), 5) # 원 그리기
    a.append([x,y])
    if(len(a)==4):
      src_pts = np.float32([a[0],a[1],a[2],a[3]]) 
      dst_pts = np.float32([[0,0], [0,600], [600,600],[600,0]]) 
      M = cv2.getPerspectiveTransform(src_pts, dst_pts) # Perspective 변환행렬 계산
      dst2 = cv2.warpPerspective(dst, M,dsize=(600, 600)) # Perspective 변환행렬 적용
      #symbol 넣기
      src2 = cv2.resize(src3, dsize=(100,100))
      rows,cols,channels = src2.shape
      roi = dst2[0:rows, 0:cols]
      gray = cv2.cvtColor(src2,cv2.COLOR_BGR2GRAY)
      ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
      mask_inv = cv2.bitwise_not(mask)
      dst2_bg = cv2.bitwise_and(roi, roi, mask = mask)
      src2_fg = cv2.bitwise_and(src2, src2, mask = mask_inv)
      dst3 = cv2.bitwise_or(dst2_bg, src2_fg)
      dst2[0:rows, 0:cols] = dst3      
      cv2.imshow('Perspective',dst2)                         
  cv2.imshow('dst', param[0])  


cv2.imshow('dst',dst)
cv2.setMouseCallback('dst',onMouse, [dst])
cv2.waitKey()
cv2.destroyAllWindows()




