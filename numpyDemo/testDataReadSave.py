import os
import numpy as np

print("data file in directory:", os.listdir("read-save-data"))

# with open("read-save-data/data.csv", "r") as f:
#     print("\n", f.read())

# data = np.loadtxt("read-save-data/data.csv", delimiter=",", skiprows=1, dtype=np.int64)
# print(data)

row_string = "20131, 10, 67, 20132, 11, 88, 20133, 12, 98, 20134, 8, 100, 20135, 9, 75, 20136, 12, 78"
data = np.fromstring(row_string, dtype=np.int64, sep=",")
data = data.reshape(6, 3)
print(data)

