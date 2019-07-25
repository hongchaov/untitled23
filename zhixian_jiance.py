import cv2 as cv
import numpy as np
import time
def line_jiance(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)#将BGR转换为灰度图像
    bianyuan = cv.Canny(gray,50,150,apertureSize=3)#得到边缘
    lines = cv.HoughLines(bianyuan,1,np.pi/180,200)
    for line in lines:
        rho,theth, = line[0]#力度
        a = np.cos(theth)
        b = np.sin(theth)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0+1000*(a))
        x2 = int(x0-1000*(-b))
        y2 = int(y0-1000*(a))
        cv.line(image,(x1,y1),(x2,y2),(0,0,255),2,)
        cv.imshow("inage_line",image)
src = cv.imread("E:\jre\cheku.jpg")

line_jiance(src)
cv.waitKey(0)
cv.destroyAllWindows()
