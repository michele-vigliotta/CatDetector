# 🐱 CatDetector

**CatDetector** is an object detection project based on **YOLOv11**, designed to detect **cats** in images, videos, and real-time webcam streams.

## 📌 Overview

The model identifies cats by drawing bounding boxes around them, along with confidence scores. It was trained on a **custom dataset** consisting of:

- **570 training images**
- **124 validation images**

The dataset was partially annotated manually.

## 🧠 Training Details

Three separate training sessions were performed on the same dataset:

1. **YOLOv11n from scratch (local):**
   - 80 epochs  
   - Configuration: `yolo11n.yaml`

2. **YOLOv11n from scratch (Google Colab):**
   - 150 epochs  
   - Configuration: `yolo11n.yaml`

3. **YOLOv11n with pretrained weights (Google Colab):**
   - 150 epochs  
   - Starting from `yolo11n.pt`

## 🛠️ Dependencies

Make sure the following packages are installed:

```bash
pip install torch torchvision opencv-python numpy
```

If you’re using the Ultralytics YOLOv11 implementation, you may also need:

```bash
pip install ultralytics
```

> ⚠️ If you're using a custom YOLOv11 version, make sure the repository is cloned and properly set up.

## 📂 Project Structure (example)

```
CatDetector/
├── dataset/
│   ├── images/
│   └── labels/
├── runs/
│   └── train/            # training output
├── predictimage.py
├── predictvideo.py
├── webcam.py
├── yolo11n.yaml
├── yolo11n.pt
└── README.md
```

## 🖼️ Example Output

*Add sample images showing detected cats with bounding boxes and confidence scores here.*
