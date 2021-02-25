import cv2
import numpy as np

image = cv2.imread("ornek-resim-2.jpg")
image_change_size = image[0:225, 0:600]

# cv2.rectangle(image,(0,100),(300,400),[0,0,255],3)   

gray = cv2.cvtColor(image_change_size, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)
# print(lines)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1,y1), (x2,y2), (0,255,0), 3)

cv2.imshow("Image",image)
cv2.imshow("Image Change Size",image_change_size)
cv2.imshow("Edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
