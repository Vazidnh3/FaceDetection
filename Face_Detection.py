import cv2

# sample file
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# defining a video capture object
Capture=cv2.VideoCapture(0)

while(True):
    _,img=Capture.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face_location=face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in face_location:
        cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('img',img)

    k=cv2.waitKey(30)
    if k==27:
        break

Capture.release()



# img=cv2.imread('img.jpg')