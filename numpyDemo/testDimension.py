import numpy as np

# cars = np.array([5, 10, 12, 6])
# print("数据：", cars, "\n维度：", cars.ndim)
#
# cars = np.array([
#     [5, 10, 12, 6],
#     [5.1, 8.2, 11, 6.3],
#     [4.4, 9.1, 10, 6.6]
# ])
#
# print("数据：\n", cars, "\n维度：", cars.ndim)


# cars = np.array([
# [
#     [5, 10, 12, 6],
#     [5.1, 8.2, 11, 6.3],
#     [4.4, 9.1, 10, 6.6]
# ],
# [
#     [6, 11, 13, 7],
#     [6.1, 9.2, 12, 7.3],
#     [5.4, 10.1, 11, 7.6]
# ],
# ])
#
# print("总维度：", cars.ndim)
# print("场地 1 数据：\n", cars[0], "\n场地 1 维度：", cars[0].ndim)
# print("场地 2 数据：\n", cars[1], "\n场地 2 维度：", cars[1].ndim)

#  一维扩展列表
# cars1 = np.array([5, 10, 12, 6])
# cars2 = np.array([5.2, 4.2])
# cars = np.concatenate([cars1, cars2])
# print(cars)


# test1 = np.array([5, 10, 12, 6])
# test2 = np.array([5.1, 8.2, 11, 6.3])
#
# # 首先需要把它们都变成二维，下面这两种方法都可以加维度
# test1 = np.expand_dims(test1, 0)
# test2 = test2[np.newaxis, :]
#
# print("test1加维度后 ", test1)
# print("test2加维度后 ", test2)
#
# # 然后再在第一个维度上叠加
# all_tests = np.concatenate([test1, test2])
# print("括展后\n", all_tests)
#
#
# print("第一维度叠加：\n", np.concatenate([all_tests, all_tests], axis=0))
# print("第二维度叠加：\n", np.concatenate([all_tests, all_tests], axis=1))


# a = np.array([
# [1,2,3],
# [4,5,6]
# ])
# b = np.array([
# [7,8],
# [9,10]
# ])
#
# print(np.concatenate([a,b], axis=1))  # 这个没问题
# # print(np.concatenate([a,b], axis=0))  # 这个会报错

# a = np.array([
#     [1, 2],
#     [3, 4]
# ])
# b = np.array([
#     [5, 6],
#     [7, 8]
# ])
# print("竖直合并\n", np.vstack([a, b]))
# print("水平合并\n", np.hstack([a, b]))


cars = np.array([
[5, 10, 12, 6],
[5.1, 8.2, 11, 6.3],
[4.4, 9.1, 10, 6.6]
])

count = 0
for i in range(len(cars)):
    for j in range(len(cars[i])):
        count += 1
print("总共多少测试数据：", count)

print("总共多少测试数据：", cars.size)

print("第一个维度：", cars.shape[0])
print("第二个维度：", cars.shape[1])
print("所有维度：", cars.shape)



