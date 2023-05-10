import numpy as np

# print(np.array([1,2,3]))
#
# my_list = [1,2,3]
# print(my_list[0])
#
# my_array = np.array([1,2,3])
# print(my_array[0])
#
# my_list[0] = -1
# my_array[0] = -1
# print(my_list)
# print(my_array)

import time

# t0 = time.time()
# # python list
# l = list(range(100))
# for _ in range(10000):
#     for i in range(len(l)):
#         l[i] += 1
#
# t1 = time.time()
# # numpy array
# a = np.array(l)
# for _ in range(10000):
#     a += 1
#
# print("Python list spend {:.3f}s".format(t1-t0))
# print("Numpy array spend {:.3f}s".format(time.time()-t1))


t0 = time.time()
# python list
l = list(range(100))
for _ in range(10000):
    l = list(map(lambda i: i+1, l))

t1 = time.time()
# numpy array
a = np.array(l)
for _ in range(10000):
    a += 1

print("Python list with map spend {:.3f}s".format(t1-t0))
print("Numpy array spend {:.3f}s".format(time.time()-t1))
