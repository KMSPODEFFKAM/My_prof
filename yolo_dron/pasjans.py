import os
import random

list_image = []
image_format = ('.png', '.jpeg', '.jpg', '.JPG')
for filename in os.listdir('dataset_xml_format/dataset_xml_format'):
    filepath = os.path.join('dataset_xml_format/dataset_xml_format', filename)
    if os.path.isfile(filepath) and filename.lower().endswith(image_format):
        list_image.append(filename)
random.shuffle(list_image)


dlina = len(list_image)
srez = round(0.8 * dlina)

i = 0
for elem_img in list_image:
    print(i)
    res = elem_img.split('.')
    name, format = res[0], res[1]
    img = f'dataset_xml_format/dataset_xml_format/{name}.{format}'
    label = f'label/{name}.txt'
    if i < srez:
        os.rename(img, f'dataset/images/train/{name}.{format}')
        os.rename(label, f'dataset/labels/train/{name}.txt')
    else:
        os.rename(img, f'dataset/images/val/{name}.{format}')
        os.rename(label, f'dataset/labels/val/{name}.txt')

    i += 1
