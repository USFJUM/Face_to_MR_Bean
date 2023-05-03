import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)
scaling_factor = 1
KMS=cv2.imread('image1.jpg')
while True:


        ret, frame = cap.read()


        frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

       

        face_rects = face_cascade.detectMultiScale(gray, 1.3, 3)
        for (x,y,w,h) in face_rects:
                print('OK>>>','x=',x,'y=',y,'(h*w)/10=',int((h*w)/5000))
                KMS=cv2.imread('image1.jpg')
                KMS=cv2.resize(KMS,(w,h+50))
                frame[y:y+h+50,x:x+w,:]=KMS
                #cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
                
                cv2.imshow('Face Detector', frame)

                c = cv2.waitKey(1)
        #if c == 27:
                # break
cap.release()
cv2.destroyAllWindows()
