import cv2
import motionBlur

angles = [-120, -60, -30, 10, 30, 60, 120]
for angle in angles:
    kernel,anchor=motionBlur.genaratePsf(20,angle)
    im = cv2.imread('original.jpg')
    motion_blur=cv2.filter2D(im,-1,kernel,anchor=anchor)
    cv2.imwrite('test{}.png'.format(angle), motion_blur)
