import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import numpy as np
from os import path, makedirs

x = np.linspace(-100, 100, 10**3)
y = -np.cos(x)*np.cos(np.pi)*np.exp(-(x-np.pi)**2)


data = ET.Element('data')
data_x = ET.SubElement(data, 'xdata')
data_y = ET.SubElement(data, 'ydata')
for i in range(x.size):
    _x = ET.SubElement(data_x, 'x')
    _x.text = str(x[i])
    _y = ET.SubElement(data_y, 'y')
    _y.text = str(y[i])
xml_data = ET.ElementTree(data)

if not path.exists('results'):
    makedirs('results')

with open("results/Res.xml", 'wb') as out:
    xml_data.write(out, encoding='utf-8')
    out.close()

plt.plot(x, y)
plt.show()
