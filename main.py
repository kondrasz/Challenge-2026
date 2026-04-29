import cv2
from ultralytics import YOLO
import torch
import os

PATH_MODELO = "best.pt"

if os.path.exists(PATH_MODELO):
    model = YOLO(PATH_MODELO)
    print(f"✅ Modelo treinado carregado com sucesso: {PATH_MODELO}")
else:
    print(f"❌ Erro: Arquivo {PATH_MODELO} não encontrado. Usando modelo padrão.")
    model = YOLO("yolov8n.pt")

# 2. Configurar Aceleração de Hardware
device = "cpu"
if torch.backends.mps.is_available():
    device = "mps"
elif torch.cuda.is_available():
    device = "0"  # GPU NVIDIA

model.to(device)

CLASSES_TREINADAS = None

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("Pressione 'q' para sair.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Erro ao acessar a câmera.")
        break

    # 4. Inferência com o modelo treinado
    results = model(
        frame,
        classes=CLASSES_TREINADAS,
        conf=0.5,
        imgsz=640,
        stream=True,
        device=device,
    )

    for r in results:
        annotated_frame = r.plot()

    cv2.imshow("FIAP Project - Detecção de EPI", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
