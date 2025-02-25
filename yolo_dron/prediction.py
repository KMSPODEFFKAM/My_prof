import cv2
from ultralytics import YOLO

model = YOLO('yolov8n_custom/weights/best.pt')

# Загрузка изображения с помощью OpenCV
image_path = 'dataset/images/val/foto05192.png'
image = cv2.imread(image_path)

# Предсказание
results = model(image)

# Визуализация результатов
for result in results:
    boxes = result.boxes.xyxy.cpu().numpy()  # Bounding boxes
    confidences = result.boxes.conf.cpu().numpy()  # Уверенность
    class_ids = result.boxes.cls.cpu().numpy().astype(int)  # Классы

    for box, conf, cls_id in zip(boxes, confidences, class_ids):
        xmin, ymin, xmax, ymax = map(int, box)
        label = f"{model.names[cls_id]} {conf:.2f}"

        # Рисуем bounding box
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

        # Добавляем текст
        cv2.putText(image, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Показываем изображение
cv2.imshow('YOLOv8 Prediction', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Сохраняем результат
cv2.imwrite('output_image1.jpg', image)