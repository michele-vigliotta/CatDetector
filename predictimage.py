from ultralytics import YOLO
import os

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


model = YOLO(path_scelto)

image_path = "images/my_cat_image.jpg"
image_dir = os.path.dirname(image_path)
image_filename = os.path.basename(image_path)
image_name, _ = os.path.splitext(image_filename)

output_filename = f"{image_name}_{modello_scelto}.jpg"
output_path = os.path.join(image_dir, output_filename)

results = model(image_path, conf=0.33)
results[0].show()  # mostra l'immagine con detection
results[0].save(filename=output_path)