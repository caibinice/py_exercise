import numpy as np


# l = [150, 166, 183, 170]
# for i in range(len(l)):
#     l[i] += 3
# print(l)
#
# print(list(map(lambda x: x+3, [150, 166, 183, 170])))
#
# a = np.array([150, 166, 183, 170])
#
# print("a + 3:", a + 3)
# print("a - 3:", a - 3)
# print("a * 3:", a * 3)
# print("a / 3:", a / 3)


#  矩阵点积（叉乘）
# a = np.array([
# [1, 2],
# [3, 4]
# ])
# b = np.array([
# [5, 6],
# [7, 8]
# ])
# #  叉乘 和b转置后矩阵的内积
# print(a.dot(b))
# print(np.dot(a, b))
#
# #  点乘 相同位置的元素乘积
# print(np.multiply(a, b))

# a = np.array([150, 166, 183, 170])
# print("最大：", np.max(a))
# print("最小：", a.min())
# print(a.sum())

# a = np.array([150, 166, 183, 170])
# print("累乘：", a.prod())
# print("总数：", a.size)
#
# a = np.array([0, 1, 2, 3])
# print("非零总数：", np.count_nonzero(a))
#
# month_salary = [1.2, 20, 0.5, 0.3, 2.1]
# print("平均工资：", np.mean(month_salary))
# print("工资中位数：", np.median(month_salary))
#
# month_salary = [1.2, 20, 0.5, 0.3, 2.1]
# print("标准差：", np.std(month_salary))


a = np.array([150, 166, 183, 170])
name = ["小米", "OPPO", "Huawei", "诺基亚"]
high_idx = np.argmax(a)
low_idx = np.argmin(a)
print("{} 最高".format(name[high_idx]))
print("{} 最矮".format(name[low_idx]))


a = np.array([150.1, 166.4, 183.7, 170.8])
print("ceil:", np.ceil(a))
print("floor:", np.floor(a))

a = np.array([150.1, 166.4, 183.7, 170.8])
print("clip:", a.clip(160, 180))
