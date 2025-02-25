import os
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

results = model.train(
    data='dataset.yaml',  # Путь к конфигурационному файлу
    epochs=100,            # Количество эпох
    batch=32,             # Размер батча
    name='yolov8n_custom',  # Имя эксперимента
    dropout=0.15,   # скипаем 15% весов для непереобучения
    project=os.getcwd()
)

