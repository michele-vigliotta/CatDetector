<h1 align="center">CatDetector</h1> 
<p align="center"> 
  <img src="https://img.shields.io/badge/Language-Python-blue.svg" alt="Python"> 
  <img src="https://img.shields.io/badge/Framework-Ultralytics%20YOLOv11-red.svg" alt="YOLOv11"> 
  <img src="https://img.shields.io/badge/Platform-Google%20Colab-yellow.svg" alt="Google Colab"> 
  <img src="https://img.shields.io/badge/Annotation-CVAT-1890FF.svg" alt="CVAT"> 
</p> 

<p> 
  <strong>CatDetector</strong> is an object detection system based on <strong>YOLOv11</strong>, designed to detect <strong>cats</strong> in images, videos, and real-time webcam streams. 
</p> 

<h2>Overview</h2> 
<p> 
  The model identifies cats by drawing bounding boxes with confidence scores. It was trained on a <strong>custom dataset</strong> consisting of: 
</p> 
<ul> 
  <li><strong>570</strong> training images</li> 
  <li><strong>124</strong> validation images</li>
</ul> 

<p>
  The dataset was partially annotated manually using CVAT.
</p> 

<h2>Training Details</h2> 

<p>Three separate training sessions were performed on the same dataset:</p>
<ol> 
  <li><strong>YOLOv11n from scratch (local):</strong><br> 80 epochs — Configuration: <code>yolo11n.yaml</code> </li> 
  <li><strong>YOLOv11n from scratch (Google Colab):</strong><br> 150 epochs — Configuration: <code>yolo11n.yaml</code> </li> 
  <li><strong>YOLOv11n with pretrained weights (Google Colab):</strong><br> 150 epochs — Starting from <code>yolo11n.pt</code> </li>
</ol> 

<h2>Dependencies</h2> 

<p>Install the required packages:</p> <pre><code>pip install ultralytics </code></pre>

<h2>Colab Scripts</h2> 

<p> The <code>colab_scripts</code> folder contains the files used for training the model on Google Colab with Google Drive integration: </p> 
<ul> 
  <li><code>CatDetector.ipynb</code>: Jupyter notebook with the full training workflow.</li> 
  <li><code>config.yaml</code>: Configuration file used during training.</li> 
</ul> 
<p> These scripts enable training using Google’s cloud resources, allowing you to leverage more powerful hardware compared to local training. </p> 

<h2>Example Output</h2> 

<p><strong>Figure 1:</strong> Cat detection using YOLOv11n from scratch (Local Model)</p> 
<p align="center"> <img src="images/my_cat_image_LocalModelFromScratch.jpg" width="600"> </p>

<p><strong>Figure 2:</strong> Cat detection using YOLOv11n from scratch (Colab Model)</p>
<p align="center"> <img src="images/my_cat_image_ColabModelFromScratch.jpg" width="600"> </p>

<p><strong>Figure 3:</strong> Cat detection using YOLOv11n pretrained (Colab Model)</p> 
<p align="center"> <img src="images/my_cat_image_ColabModelPretrained.jpg" width="600"> </p>
