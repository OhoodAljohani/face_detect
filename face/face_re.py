import cv2
face_cascade = cv2.CascadeClassifier('face_detector.xml')
img=cv2.imread("king_salman/king.jpg")
faces = face_cascade.detectMultiScale(img, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces: 
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
  # Export the result
cv2.imwrite("face_detected.png", img) 
print('Successfully saved')

