import cv2
import time
import mediapipe as mp

video_capture = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.45)

# Threshold to classify it as a face
# Default value is 0.5


pTime=0

while True:

	ret, frame = video_capture.read()

	imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	results = faceDetection.process(imgRGB)
	#print(results)

	if(results.detections):
		for id, detection in enumerate(results.detections):
			# mpDraw.draw_detection(frame, detection)
			# print(id, detection)
			# print(detection.score)
			# print(detection.location_data.relative_bounding_box)
			bboxC = detection.location_data.relative_bounding_box
			img_h, img_w, img_c = frame.shape

			bbox = int(bboxC.xmin * img_w), int(bboxC.ymin * img_h), \
					int(bboxC.width * img_w), int(bboxC.height * img_h)

			cv2.rectangle(frame, bbox, (255, 0, 255), 2)
			cv2.putText(frame, f'{int(detection.score[0]*100)}%', 
						(bbox[0],bbox[1]-20), font, 0.8, (255,0,255), 2)



	cTime=time.time()
	fps = (1/(cTime-pTime))
	pTime=cTime

	frame = cv2.putText(frame, 'FPS: ' + str(int(fps)), (50,50), font, 0.8, (128,255,0), 2)


	cv2.imshow('Video', frame)



	if(cv2.waitKey(1) & 0xFF == ord('q')):
		break

	

video_capture.release()
cv2.destroyAllWindows()