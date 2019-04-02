# 20171049 컴퓨터학과 전유현
# 2번 테스트1

import cv2
import numpy as np

a = []
def onMouse(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽 마우스 클릭시
    cv2.circle(param[0], (x, y), 5, (255,255,0), 3) # 원 그리기
    a.append([x,y])
    if(len(a)==4):
      src_pts = np.float32([a[0],a[1],a[2],a[3]]) 
      dst_pts = np.float32([[0,0], [0,600], [600,600],[600,0]]) 
      M = cv2.getPerspectiveTransform(src_pts, dst_pts) # Perspective 변환행렬 계산
      dst2 = cv2.warpPerspective(dst, M,dsize=(600, 600)) # Perspective 변환행렬 적용
      cv2.imshow('Perspective',dst2) # dst2 출력
                        
  cv2.imshow('dst', param[0])  

imageFile = './a4.jpg'
img = cv2.imread(imageFile) #color로 imageFile 읽기
dst = cv2.resize(img, dsize=(600, 600)) # img (600,600) 크기로 조절
cv2.imshow('dst',dst)

cv2.setMouseCallback('dst',onMouse, [dst])
cv2.waitKey()
cv2.destroyAllWindows()




