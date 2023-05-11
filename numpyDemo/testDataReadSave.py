import os
import numpy as np

# print("data file in directory:", os.listdir("read-save-data"))

# with open("read-save-data/data.csv", "r") as f:
#     print("\n", f.read())

data = np.loadtxt("read-save-data/data.csv", delimiter=",", skiprows=1, dtype=np.int64)
# print(data)

# row_string = "20131, 10, 67, 20132, 11, 88, 20133, 12, 98, 20134, 8, 100, 20135, 9, 75, 20136, 12, 78"
# data = np.fromstring(row_string, dtype=np.int64, sep=",")
# data = data.reshape(6, 3)
# print(data)

# print("numpy data:\n", data)
# np.savetxt("read-save-data/save_data.csv", data, delimiter=",", fmt='%s')
#
# print("data file in directory:", os.listdir("read-save-data"))
# with open("read-save-data/save_data.csv", "r") as f:
#     print("\n", f.read())

# np.save("read-save-data/save_data.npy", data)
#
# print("data file in directory:", os.listdir("read-save-data"))
# npy_data = np.load("read-save-data/save_data.npy")
# print(npy_data)


# train_data = np.array([1,2,3])
# test_data = np.array([11,22,33])
#
# np.savez("read-save-data/save_data.npz", train=train_data, test=test_data)
# print("data file in directory:", os.listdir("read-save-data"))

train_data = np.array([1,2,3])
test_data = np.array([11,22,33])
#
# np.savez("read-save-data/save_data.npz", train=train_data, test=test_data)
# print("data file in directory:", os.listdir("read-save-data"))
#
# npz_data = np.load("read-save-data/save_data.npz")
# print("train:", npz_data["train"])
# print("test:", npz_data["test"])


np.savez_compressed("read-save-data/save_data_compressed.npz", train=train_data, test=test_data)
print("data file in directory:", os.listdir("read-save-data"))

npz_data_compressed = np.load("read-save-data/save_data_compressed.npz")
print("train:", npz_data_compressed["train"])
print("test:", npz_data_compressed["test"])

import os

print("compressed file size:", os.path.getsize("read-save-data/save_data_compressed.npz"))
print("original file size:", os.path.getsize("read-save-data/save_data.npz"))





