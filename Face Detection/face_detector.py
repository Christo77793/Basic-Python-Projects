import cv2

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.imread("dp.jpg", 1)
image = cv2.resize(image, (500, 600))

grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grey = cv2.resize(grey, (500, 600))

"""
cv2.imshow("Original", image)
cv2.imshow("Grey Image", grey)
"""

faces = cascade.detectMultiScale(grey,
scaleFactor= 1.05,
minNeighbors=3)

for x, y, w, h in faces:
    image = cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 3)

final_image = cv2.resize(image, (500, 600))
cv2.imshow("Face Detected", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()