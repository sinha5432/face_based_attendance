# Face extraction

This repo consists of two python files, which uses following method to extract faces:
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

As of now, MTCNN in better among these two.
