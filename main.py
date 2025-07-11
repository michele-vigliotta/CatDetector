from ultralytics import YOLO

# Create a new YOLO model from scratch
model = YOLO("yolo11n.yaml")



# Train the model using the 'config.yaml' dataset 
# patience=10 significa che il training si ferma se il modello non migliora per 10 epochs consecutive
results = model.train(data="config.yaml", epochs=50, patience=10)

