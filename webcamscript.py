from ultralytics import YOLO
import cv2

# Carica il tuo modello allenato
model = YOLO("runs/detect/train/weights/best.pt")

# Avvia la webcam
cap = cv2.VideoCapture(0)  # 0 = webcam predefinita

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Rileva gatti nel frame
    results = model(frame)
    
    # Mostra i risultati
    annotated_frame = results[0].plot()
    cv2.imshow('Rilevamento Gatti', annotated_frame)
    
    # Premi 'q' per uscire
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()