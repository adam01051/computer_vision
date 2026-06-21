# print("hello")
# import cv2

# cap = cv2.VideoCapture(0)
# while True:
#     success, frame = cap.read()
#     if not success:
#         print("Cannot read frame")
#         break
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        
#     cv2.imshow("Original", frame)
#     cv2.imshow("gray", gray)
    
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()

# ================================


import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


while True:
    success, frame = cap.read()
    if not success:
        print("Cannot read frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)


    cv2.imshow("real-time face detection",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# cap.release()
# cv2.destroyAllWindows()


        

