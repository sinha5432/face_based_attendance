# Face Recognition

This repo has Data, iPython Notebooks and models to differentiate among:

<ul>
  <li> Barack Obama </li>
  <li> Donald Trump </li>
  <li> Queen Elizabeth II </li>
  <li> Bill Gates </li>
</ul>

On live Video feed.<br>

VGG16 is used as base CNN model over which fully connected DL layers are present.<br>

Following are the functionalities of each iPython Notebook:

<ul>
  <li> Data_collection.ipynb : To collect data of person to be recognised. 
                               It can collect data from a folder as well as from a live video feed. </li>
  <li> face_detection_custom.ipynb : Definition of model architecture and training is performed in this notebook.</li>
  <li> Prediction.ipynb : Code to detect faces and output recognised person's name if he/she is present in collected data. </li>
</ul>
<br>
**Deep Learning method gives 5 FPS at max when run on CPU**

This method is slow, but is quite accurate.
---
Methods to extract faces out of images:
  <ul>
    <li>Haar Cascade frontal face detector</li>
    <li>MTCNN (Multi-task Cascaded Convolutional Neural Networks)</li>
  </ul>
As of now, they are set to operate with system's default webcam.
<br>
<ul>
<li>For haar cascade code:</li>
<p>Sensitivity of face detection can be changed by changing minNeighbours argument on line 19.<br>
It can only detect front facing faces<br>
Speed for this algorithm was around 20 fps on my system</p>

<li>For MTCNN code:</li>
  <p>Sensitivity of detection can be changed by modifying argument of faceDetector on line 10.<br>
     It is a much more robust algorithm as it can detect faces in any orientation.<br>
     Processing speed was around 30fps on my system.</p>
</ul>

MTCNN was proved to be better among these two and is utilised for Data collection.
