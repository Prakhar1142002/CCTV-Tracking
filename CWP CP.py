import cv2
import numpy as np

img = cv2.imread("lena.jpg", -1)
print(img)

cv2.imshow("Sample", img)
k = cv2.waitKey()

if k == 27:   # escape button's ord
    cv2.destroyAllWindows()
elif k == ord("q"):
    cv2.imwrite("lena_copy.png", img)
    cv2.destroyAllWindows()

# imgblur = cv2.GaussianBlur(img, (7,7), 0)
# imgcan = cv2.Canny(img, 100, )
# img = np.zeros(512,512,)