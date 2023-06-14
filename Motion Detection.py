# Motion detection code_code 1
import cv2

cwp = cv2.VideoCapture("vtest.avi")

ret, frame1 = cwp.read()
ret2, frame2 = cwp.read()

while cwp.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900:
            continue

        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "P3 Group: SPRINT", (15, 35), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 0), 3)

    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv2.imshow("SPRINT CCTV Footage", frame1)
    frame1 = frame2
    ret, frame2 = cwp.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cwp.release()


# # Hand Co-ordinate Tracker_code 2
# import cv2
# import mediapipe as mp
# import time
# #defining the objects
# cap = cv2.VideoCapture(0)#for webCam
# mpHands = mp.solutions.hands#formality
# hands = mpHands.Hands(False)#creating the object(false = default parameter)
# mpDraw = mp.solutions.drawing_utils#inbuid in pipe
#
#
# while True:
#     success, img = cap.read()#for reading the image
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#for converting bgr to rgb image bcoz hands accept only rgb
#     results = hands.process(imgRGB)#proecess the frame and give us result
#     print(results.multi_hand_landmarks)#to check something is detected or not
#
#     if results.multi_hand_landmarks:
#         for handLms in results.multi_hand_landmarks:#extracting information of each hand
#             mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)#for drawing the image#LMs used for there is single hand
#                                                 #connecting the all marks
#
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)
#
#
# # Face Detection_code 3
# import cv2
#
#
# cascPath = 'haarcascade_frontalface_default.xml'
# facecascade = cv2.CascadeClassifier(cascPath)
#
# img = cv2.imread('FACE.jpeg')
# cv2.imshow('Original',img)
#
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces = facecascade.detectMultiScale(gray,1.4,1)
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
# cv2.imshow('image',img)
# cv2.waitKey()