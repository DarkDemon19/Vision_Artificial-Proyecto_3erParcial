from ultralytics import YOLO

# 1. Cargamos el modelo matemático base (se descargará solo la primera vez)
model = YOLO('yolov8n.pt') 

# 2. Iniciamos el entrenamiento apuntando al archivo de configuración
results = model.train(
    data='data.yaml',    # Archivo que le dice a YOLO dónde están tus carpetas
    epochs=50,           # Cantidad de vueltas de entrenamiento que dará
    imgsz=640            # Tamaño estándar de procesamiento de las imágenes
)