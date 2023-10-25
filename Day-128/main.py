import cv2

favce_cap = cv2.Cascading_Face_Detector("haarcascade_frontalface_default.xml")

video_cap = cv2.VideoCapture(0)

while True:
  ret, video = video_cap.read()
  dol = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
  faces = favce_cap.detectMultiScale(dol)
  cv2.imshow('Video', video)
  for (x, y, w, h) in faces:
    cv2.rectangle(video, (x, y), (x+w, y+h), (0, 255, 0), 2)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


video_cap.release()
