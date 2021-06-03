import cv2
import time


cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
font = cv2.FONT_HERSHEY_SIMPLEX

video_capture = cv2.VideoCapture(0)

while True:

	init_time=time.time()

	ret, frame = video_capture.read()

	grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=8, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	time_elapsed = time.time()-init_time
	fps = int(1/time_elapsed)

	frame = cv2.putText(frame, 'FPS: ' + str(fps), (50,50), font, 0.8, (128,255,0), 2)


	cv2.imshow('Video', frame)



	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	

video_capture.release()
cv2.destroyAllWindows()
