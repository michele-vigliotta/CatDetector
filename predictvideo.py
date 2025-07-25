
import cv2
from ultralytics import YOLO
from pathlib import Path


def process_video_with_yolo(model_path, input_video_path, conf_threshold):
    """
    Processa un video con un modello YOLO e salva il video con i detection box
    nella stessa cartella del video input
    """
    
    # Carica il modello YOLO
    model = YOLO(model_path)
    
    # Genera il nome del file output
    input_path = Path(input_video_path)
    output_path = input_path.parent / f"{input_path.stem}_{modello_scelto}{input_path.suffix}"
    
    # Apri il video di input
    cap = cv2.VideoCapture(input_video_path)
    
    # Ottieni informazioni sul video
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Configura il writer per il video di output
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))
    
    # Processa frame per frame
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Esegui la detection e disegna i box
        results = model(frame, conf=conf_threshold)
        annotated_frame = results[0].plot()
        
        # Scrivi il frame processato
        out.write(annotated_frame)
    
    # Rilascia le risorse
    cap.release()
    out.release()
    cv2.destroyAllWindows()


# Modifica questi percorsi con i tuoi file

INPUT_VIDEO = "videos/mycat_test.mp4"
CONF_THRESHOLD = 0.1  # mostra i box solo quando é sicuro almeno per il 30%

# lista modelli con path
model_options = {
    "LocalModelFromScratch": "runs/detect/train/weights/best.pt",
    "ColabModelFromScratch": "runs_colab_fromscratch/content/runs/detect/train/weights/best.pt",
    "ColabModelPretrained": "runs_colab_pretrained/content/runs/detect/train2/weights/best.pt"
}

print("Seleziona un modello:")
for i, nome_modello in enumerate(model_options, start=1):
    print(f"{i}. {nome_modello}")

nomi_modelli = list(model_options.keys())
while True:
    try:
        scelta = int(input("Inserisci il numero del modello (1-3): "))
        if 1 <= scelta <= len(nomi_modelli):
            modello_scelto = nomi_modelli[scelta - 1]
            path_scelto = model_options[modello_scelto]
            break
        else:
            print("Numero non valido, riprovare")
    except ValueError:
        print("Inpunt non valido, inserire un numero")

MODEL_PATH = path_scelto
process_video_with_yolo(MODEL_PATH, INPUT_VIDEO, CONF_THRESHOLD)