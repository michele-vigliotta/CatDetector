from ultralytics import YOLO

# Create a new YOLO model from scratch
model = YOLO("yolo11n.yaml")



# Train the model using the 'config.yaml' dataset 
# patience=10 significa che il training si ferma se il modello non migliora per 10 epochs consecutive
results = model.train(data="config.yaml", 
                      epochs=80, 
                      patience=15, #si ferma se dopo 15 epoch non migliora
                      batch=24, #24 immagini alla volta
                      imgsz=640,
                      workers=4,
                      save_period=10 #salva il modello ogni 10 epoch
                      )

