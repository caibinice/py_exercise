import random
import numpy as np
import matplotlib.pyplot as plt

def draw_line(d):
    plt.figure()
    plt.plot(d)
    plt.show()

# print(random.random())
# print(random.randint(1, 10))
# # 随机生成 [0, 1) 之间的数
# dim1, dim2 = 3, 2
# print(np.random.rand(dim1, dim2)) # 你还能继续添加 dim3 或更多
#
# print(np.random.random([dim1, dim2]))
#
# # 按标准正态分布生成随机数
# print(np.random.randn(dim1, dim2))
# 随机整数，左闭右开
# print(np.random.randint(low=-3, high=6, size=10))

# data = np.array([2,1,3,4,6])
# print("选一个：", np.random.choice(data))
# print("选多个：", np.random.choice(data, size=3))
# print("不重复地选多个(不放回)：", np.random.choice(data, size=5, replace=True))
# print("带权重地选择：", np.random.choice(data, size=10, p=[0,0,0.1,0.2,0.7]))


# data_copy = np.copy(data)
# np.random.shuffle(data)
# print("源数据：", data_copy)
# print("shuffled:", data)

# print("直接出乱序序列：", np.random.permutation(10))
# data = np.arange(12).reshape([6,2])
# print(data)
# print("多维数据在第一维度上乱序：", np.random.permutation(data))


# # (均值，方差，size)
# data1 = np.random.normal(1, 0.2, 10)
# print("正态分布：", data1)
# draw_line(data1)
# # (最低，最高，size)
# data2 = np.random.uniform(-1, 1, 10)
# print("均匀分布：", data2)
# draw_line(data2)

# seed(1) 代表的就是 1 号随机序列
# np.random.seed(1)
# print(np.random.randint(2, 10, size=3))
# print(np.random.randint(2, 10, size=3))

np.random.seed(2)
print(np.random.randint(2, 10, size=3))
np.random.seed(2)
print(np.random.randint(2, 10, size=10))
