from ultralytics import YOLO
model = YOLO("runs/detect/train/weights/best.pt")
results = model("images/my_cat_image.jpg", conf=0.1)
results[0].show()  # mostra l'immagine con detection