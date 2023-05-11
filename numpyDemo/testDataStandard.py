import numpy as np

# zeros = np.zeros([2, 3])
# print("zeros:\n", zeros)
#
# ones = np.ones([3, 2])
# print("\nones:\n", ones)
#
# nines = np.full([2, 3], 9)
# print(nines)

data = np.array([
    [1, 2, 3],
    [4, 5, 6]
], dtype=np.int64)

ones = np.ones(data.shape, dtype=data.dtype)
ones_like = np.ones_like(data)

# print("ones:", ones.shape, ones.dtype)
# print("ones_like:", ones_like.shape, ones_like.dtype)
# print("ones_like value:\n", ones_like)
#
# print(np.zeros_like(data))
# print(np.full_like(data, 6))
#
# print("python range:", list(range(5)))
# print("numpy arange:", np.arange(5))

# (start, end, step)
# print("python range:", list(range(3, 10, 2)))
# print("numpy arange:", np.arange(3, 10, 2))


# (start, end, num)
# print("linspace:", np.linspace(-1, 1, 5))
# 划分成5个区域
# print("5 segments:", np.linspace(-1, 1, 5, endpoint=False))

# 随机数生成，速度比ones full zeros 快
# print(np.empty([4,3]))
#
# import time
# t0 = time.time()
#
# for _ in range(10000):
#     _ = np.ones([100, 100])
#
# t1 = time.time()
# for _ in range(10000):
#     _ = np.empty([100, 100])
#
# t2 = time.time()
# print("ones time:", t1 - t0)
# print("empty time:", t2 - t1)


import random

empty = np.empty([2,3])
print("empty before:\n", empty)
data = np.arange(6).reshape([2, 3])
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        empty[i, j] = data[i, j] * random.random()
print("empty after:\n", empty)
