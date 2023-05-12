import numpy as np
import matplotlib.pyplot as plt

# data = np.random.rand(4, 3)
# weights = np.random.rand(3, 2)
# output = np.dot(data, weights)
#
# print("data shape:", data.shape)
# print("weights shape:", weights.shape)
# print("output shape:", output.shape)

#  回归问题
# student = np.array([[1,2,3]])
# model = np.random.rand(3, 1)
# score = np.dot(student, model)
# print(model)
# print(score)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


#  分类问题
# student = np.array([[0.1,0.2,-0.3]])
# model = np.random.rand(3, 1)
# output = np.dot(student, model)
#
# # 用 level 表示是否及格
# result = sigmoid(output)
# if result < 0.5:
#     level = "不及格"
# else:
#     level = "及格"
# print(level)


def draw_scatter(x, y):
    plt.scatter(x.ravel(), y.ravel())
    plt.show()


x = np.linspace(-1, 1, 10)[:, None]     # shape [10, 1]
y = np.random.normal(loc=0, scale=0.2, size=[10, 1]) + x   # shape [10, 1]

# draw_scatter(x, y)

def layer(in_dim, out_dim):
    weights = np.random.normal(loc=0, scale=0.1, size=[in_dim, out_dim])
    bias = np.full([1, out_dim], 0.1)
    return {"w": weights, "b": bias}


# 模型
l1 = layer(1, 3)
l2 = layer(3, 1)

# # 计算
# o = x.dot(l1["w"]) + l1["b"]
# print("第一层出来后的 shape:", o.shape)
#
# o = o.dot(l2["w"]) + l2["b"]
# print("第二层出来后的 shape:", o.shape)
#
# print("output:", o)
# draw_scatter(x, o)


def relu(x):
    return np.maximum(0, x)


def tanh(x):
    return np.tanh(x)


# 第一层
o = x.dot(l1["w"]) + l1["b"]

# 可以在这里添加激活函数，增强非线性拟合能力
o = tanh(o)

# 第二层
o = o.dot(l2["w"]) + l2["b"]

print(o.shape)
draw_scatter(x, o)

