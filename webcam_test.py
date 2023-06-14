import cv2
import datetime

cwp = cv2.VideoCapture(0)

while True:
    ret, frame = cwp.read()
    cv2.imshow("Cam", frame)

    # dt = str(datetime.datetime.now())
    # frame = cv2.putText(frame, dt)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cwp.release()
cv2.destroyAllWindows()
