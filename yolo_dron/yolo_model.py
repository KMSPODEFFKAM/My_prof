import cv2
from ultralytics import YOLO
import numpy as np

model = YOLO('yolov8n.pt')
name_photo = 'dataset/image/train/foto00987.png'
results = model(name_photo)

for result in results:
    boxes = result.boxes  # Объекты типа Boxes содержат информацию о bounding boxes
    for box in boxes:
        # Координаты ограничивающей рамки (в формате xyxy: x1, y1, x2, y2)
        xyxy = box.xyxy
        # Координаты центра и размеры (в формате xywh: x_center, y_center, width, height)
        xywh = box.xywh
        # Класс объекта
        class_id = box.cls
        # Уверенность
        confidence = box.conf

    print(f"Объект класса {class_id} с уверенностью {confidence} в рамке {xyxy}")

    dict_param = {'Class': str(int(class_id.item())),
                  'Accuracity': str(round(confidence.item(), 3))
                  }

    img = cv2.imread(name_photo)
    x_size, y_size, kanals = img.shape
    xyxy = np.array(xyxy[0, :])
    x1, y1, x2, y2 = [round(elem) for elem in xyxy]

    cv2.rectangle(img, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)

    x = x_size // 2
    y = y_size // 2
    font_scale = 0.5
    color = (0, 0, 0)  # Черный
    thickness = 1

    i = 0
    for key, var in dict_param.items():
        cv2.putText(img, f'{key} = {var}', (x, y + 15 * i), cv2.FONT_HERSHEY_SIMPLEX,
                    font_scale, color, thickness, cv2.LINE_AA)
        i += 1


    cv2.imshow('Image with Rectangle', img)
    cv2.waitKey(0)  # Ждет нажатия клавиши
    cv2.destroyAllWindows()