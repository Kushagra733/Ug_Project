import numpy as np
import matplotlib.pyplot as plt
import csv

csv_file = './simhadri_gt1r_6005792.csv'

x_data = []
y_data = []


with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  
    for row in csv_reader:
         values = row[0].split('\t')
         if len(values) == 2:
            x_value = float(values[0].replace('E', 'e'))  
            y_value = float(values[1].replace('E', 'e'))  
            x_data.append(x_value)
            y_data.append(y_value)

if x_data and y_data:
    data = np.array([x_data, y_data]).T 
else:
    data = np.array([])   




plt.scatter(data[:, 0], data[:, 1], s=10, c='b', marker='o', label='Data Points')
plt.xlabel('X-Axis Label')
plt.ylabel('Y-Axis Label')
plt.title('Scatter Plot of Data')
plt.legend()
plt.grid(True)
plt.show()

