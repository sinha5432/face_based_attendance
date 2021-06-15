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


direc = r'F:/python_notebooks/face_based_attendance/unprocessed_data/Barack_Obama/'


frame = cv2.imread(direc + 'Obama1098.jpg')

# imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# results = faceDetection.process(imgRGB)
# #print(results)

# if(results.detections):
# 	for id, detection in enumerate(results.detections):
# 		bboxC = detection.location_data.relative_bounding_box
# 		img_h, img_w, img_c = frame.shape

# 		xmin = int(bboxC.xmin * img_w)
# 		ymin = int(bboxC.ymin * img_h)
# 		w = int(bboxC.width * img_w)
# 		h = int(bboxC.height * img_h)

# 		new_frame = frame[ymin:ymin+h, xmin:xmin+w]



cv2.imshow('Video', frame)
cv2.moveWindow('Video', 90,50)

cv2.waitKey(0)


cv2.destroyAllWindows()