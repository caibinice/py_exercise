import numpy as np
import timeit
from functools import partial


# a = np.arange(1, 7).reshape((3,2))
# a_view = a[:2]
# a_copy = a[:2].copy()
# print(a_view)
# print(a_copy)
# a_copy[1,1] = 0
# print("在 copy 上修改数据，不会影响源数据：\n", a)
#
# a_view[1,1] = 0
# print("在 view 上修改数据，会影响'窗里'的源数据：\n", a)


def get_run_time(func, *args):
    repeat = 3
    number = 200
    return min(timeit.Timer(partial(func, *args)).repeat(repeat=repeat, number=number)) / number


# a = np.random.rand(1000, 1000)
# b = np.random.rand(1000, 1000)
#
#
# def f1():
#     global b
#     # 这会产生新的 b
#     b = 2*b
#
# def f2():
#     global a
#     # 这不会产生新的 a
#     a *= 2    # 和 a[:] *= 2 一样
#
#
# print('%.6f - b = 2*b' % get_run_time(f1))
# print('%.6f - a *= 2' % get_run_time(f2))


# def f1():
#     a.flatten()
#
#
# def f2():
#     b.ravel()
#
#
# print(a.flatten())
# print(b.ravel())
# print('%.6f - flatten' % get_run_time(f1))
# print('%.6f - ravel' % get_run_time(f2))

# # view的方式
# a = np.zeros([100, 100])
# a_view1 = a[1:2, 3:6]    # 切片 slice
# a_view2 = a[:100]        # 同上
# a_view3 = a[::2]         # 跳步
# a_view4 = a.ravel()      # 上面提到了
# # 我只能想到这些, 如果还有请大家在评论里提出
#
# # copy的方式
# a = np.zeros([2, 2])
# a_copy2 = a[[True, True], [False, True]]  # 用 mask
# a = np.zeros([100, 100])
# a_copy1 = a[[1,4,6], [2,4,6]]   # 用 index 选
# a_copy3 = a[[1,2], :]        # 虽然 1,2 的确连在一起了, 但是他们确实是 copy
# a_copy4 = a[a[1,:] != 0, :]  # fancy indexing
# a_copy5 = a[np.isnan(a[:,0]), :]  # fancy indexing


# a = np.random.rand(1000000, 10)
# indices = np.random.randint(0, len(a), size=10000)
#
#
# def f1():
#     # fancy indexing
#     _ = a[indices]
#
#
# def f2():
#     # take使用 np.take(), 替代用 index 选数据的方法。
#     _ = np.take(a, indices, axis=0)
#
#
# print('%.6f - [indices]' % get_run_time(f1))
# print('%.6f - take' % get_run_time(f2))
#


# 使用 np.compress(), 替代用 mask 选数据的方法。
# a = np.random.rand(10000, 10)
# print(a.shape)
# mask = a[:, 0] < 0.5
#
#
# def f1():
#     _ = a[mask]
#
#
# def f2():
#     _ = np.compress(mask, a, axis=0)
#
#
# print('%.6f - [mask]' % get_run_time(f1))
# print('%.6f - compress' % get_run_time(f2))


# a = np.zeros([10000, 10])
#
#
# def f1(a):
#     a = a + 1
#
#
# def f2(a):
#     a = np.add(a, 1)
#
#
# print('%.6f - a + 1' % get_run_time(f1, a))
# print('%.6f - np.add(a, 1)' % get_run_time(f2, a))


# a = np.zeros([2, ])
# a_copy = np.add(a, 1)  # copy 发生在这里
# print(a, a_copy)
#
# b = np.zeros([2, ])
# c = np.zeros_like(b)  # copy 发生在这里
# np.add(b, 1, out=c)
# print(b, c)

a = np.zeros([1000, 1000])
b = np.zeros_like(a)
c = np.zeros_like(a)


def f1():
    a[:] = np.add(a, 1)  # 把计算结果赋值回原数据


def f2():
    np.add(b, 1, out=b)  # 把计算结果赋值回原数据


def f3():
    _c = np.add(c, 1)  # 把计算结果赋值到新数据


print('%.6f - without out' % get_run_time(f1))
print('%.6f - out' % get_run_time(f2))
print('%.6f - new data' % get_run_time(f3))
