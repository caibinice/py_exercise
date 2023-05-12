import numpy as np
import matplotlib.pyplot as plt


def draw_scatter(x, y):
    plt.scatter(x.ravel(), y.ravel())
    # plt.show() 最后才调用，这样可以在一个画布显示两个曲线


def draw_line(x, y):
    idx = np.argsort(x.ravel())
    plt.plot(x.ravel()[idx], y.ravel()[idx])
    # plt.show()


def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):  # 导数
    return np.where(x > 0, np.ones_like(x), np.zeros_like(x))


def tanh(x):
    return np.tanh(x)


def tanh_derivative(x):  # 导数
    return 1 - np.square(np.tanh(x))


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):  # 导数
    o = sigmoid(x)
    return o * (1 - o)


x = np.linspace(-1, 1, 30)[:, None]  # shape [30, 1]
y = np.random.normal(loc=0, scale=0.2, size=[30, 1]) + x ** 2  # shape [30, 1]


# draw_scatter(x, y)

# 搭建模型
def layer(in_dim, out_dim):
    weights = np.random.normal(loc=0, scale=0.1, size=[in_dim, out_dim])
    bias = np.full([1, out_dim], 0.1)
    return {"w": weights, "b": bias}


def backprop(dz, layer1, layer_in):
    gw = layer_in.T.dot(dz)
    gb = np.sum(dz, axis=0, keepdims=True)
    new_dz = dz.dot(layer1["w"].T)
    layer1["w"] += learning_rate * gw
    layer1["b"] += learning_rate * gb
    return new_dz


l1 = layer(1, 10)
l2 = layer(10, 1)


# def predict(x):
#     o1 = x.dot(l1["w"]) + l1["b"]
#     o2 = o1.dot(l2["w"]) + l2["b"]
#     return [o1, o2]
#
#
# # 训练 300 次
# learning_rate = 0.01
# for i in range(300):
#     # 前向预测
#     o1, o2 = predict(x)
#
#     # 误差计算
#     if i % 10 == 0:
#         average_cost = np.mean(np.square(o2 - y))
#         print(average_cost)
#
#     # 反向传播，梯度更新
#     dz2 = -2 * (o2 - y)  # 输出误差 (o2 - y)**2 的导数
#     dz1 = backprop(dz2, l2, o1)
#     _ = backprop(dz1, l1, x)
#
# draw_line(x, predict(x)[-1])
# draw_scatter(x, y)


def predict_2(xx):
    k1 = xx.dot(l1["w"]) + l1["b"]
    aa1 = relu(k1)  # 这里我添加了一个激活函数
    k2 = aa1.dot(l2["w"]) + l2["b"]
    return [k1, aa1, k2]


# 训练 300 次
learning_rate = 0.01
for i in range(300):
    # 前向预测
    o1, a1, o2 = predict_2(x)

    # 误差计算
    if i % 10 == 0:
        average_cost = np.mean(np.square(o2 - y))
        print(average_cost)

    # 反向传播，梯度更新
    dz2 = -2 * (o2 - y)  # 输出误差 (o2 - y)**2 的导数
    dz1 = backprop(dz2, l2, a1)
    dz1 *= relu_derivative(o1)  # 这里要添加对应激活函数的反向传播
    _ = backprop(dz1, l1, x)

draw_line(x, predict_2(x)[-1])
draw_scatter(x, y)



plt.show()
