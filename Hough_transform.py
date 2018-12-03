import cv2
import glob
import numpy as np
img_dir = "F:/ML_and_AI/CV/Hough Transform/Data/*.jpg"
values = {"8":1,"16":5,"32":10,"64":25}
with open("sample.txt","w+") as f:
    f.write("Id,Expected\n")

images = [print(cv2.imread(file,0)) for file in glob.glob(img_dir)]

for img in images:
    print(img.shape)
    edge = cv2.Canny(img,100,200)
    print(edge.shape)
    cv2.imshow("do you think you are funny???",edge)
    cv2.waitkey(0)
