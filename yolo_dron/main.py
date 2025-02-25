import os

from lxml import etree

xml_files = []

path = 'dataset_xml_format/dataset_xml_format'

for file in os.listdir(path):
    filepath = os.path.join(path, file)
    if os.path.isfile(filepath) and file.lower().endswith('.xml'):
        xml_files.append(file)

for elem in xml_files:
    print(elem)
    data = []

    tree = etree.parse(f'dataset_xml_format/dataset_xml_format/{elem}')
    root = tree.getroot()

    for element_size in root.findall('size'):
        x_size = int(element_size.find('width').text)
        y_size = int(element_size.find('height').text)

    for element_param in root.findall('object'):
        target = element_param.find('truncated').text
        size = element_param.find('bndbox')
        x_min_n = int(size.find('xmin').text) / x_size
        x_max_n = int(size.find('xmax').text) / x_size
        y_min_n = int(size.find('ymin').text) / y_size
        y_max_n = int(size.find('ymax').text) / y_size

        width = x_max_n - x_min_n
        height = y_max_n - y_min_n
        x_center = x_min_n + (width / 2)
        y_center = y_min_n + (height / 2)

        data_param = [target, x_center, y_center, width, height]
        data.append(data_param)

    res = elem.split('.')[0]

    with open(f'label/{res}.txt', 'w') as file:
        for date in data:
            date = [str(elem) for elem in date]
            write = file.writelines(' '.join(date) + '\n')
