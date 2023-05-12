import numpy as np
import matplotlib.pyplot as plt


def draw_scatter(x, y):
    plt.scatter(x.ravel(), y.ravel())
    # plt.show() 最后才调用，这样可以在一个画布显示两个曲线


def draw_line(x, y):
    idx = np.argsort(x.ravel())
    plt.plot(x.ravel()[idx], y.ravel()[idx])
    # plt.show()


# 数据
x = np.linspace(-1, 1, 10)[:, None]  # shape [10, 1]
y = np.random.normal(loc=0, scale=0.2, size=[10, 1]) + x  # shape [10, 1]


# draw_scatter(x, y)


# 添加神经层
def layer(in_dim, out_dim):
    weights = np.random.normal(loc=0, scale=0.1, size=[in_dim, out_dim])
    bias = np.full([1, out_dim], 0.1)
    return {"w": weights, "b": bias}


# # 简单模型
# l1 = layer(1, 5)
# l2 = layer(5, 1)
#
# # 计算
# o = x.dot(l1["w"]) + l1["b"]
# print("第一层出来后的 shape:", o.shape)
#
# o = o.dot(l2["w"]) + l2["b"]
# print("第二层出来后的 shape:", o.shape)
#
# print("output:", o)
# draw_scatter(x, o)


l1 = layer(1, 3)
l2 = layer(3, 1)


def predict(xx):
    k1 = xx.dot(l1["w"]) + l1["b"]
    k2 = k1.dot(l2["w"]) + l2["b"]
    return [k1, k2]


# draw_line(x, predict(x)[-1])
# draw_scatter(x, y)

# 梯度反向更新
# 计算每一层神经层的更新幅度，并按照学习率来更新网络参数，让网络对数据拟合得越来越好。
# 这里面就涉及到了 Numpy 的矩阵转置 .T，也有累加的操作 .sum()。 每次调用 backprop() 功能，
# 我们实际上在干的事就是去计算每一层 w 和 b 的梯度 gw 和 gb。然后将梯度误差在传递到前面的一层去。
def backprop(dz, layer1, layer_in):
    gw = layer_in.T.dot(dz)
    gb = np.sum(dz, axis=0, keepdims=True)
    new_dz = dz.dot(layer1["w"].T)
    layer1["w"] += learning_rate * gw
    layer1["b"] += learning_rate * gb
    return new_dz


# 训练 50 次
learning_rate = 0.01
for i in range(50):
    # 前向预测
    o1, o2 = predict(x)

    # 误差计算
    if i % 10 == 0:
        average_cost = np.mean(np.square(o2 - y))
        print(average_cost)

    # 反向传播，梯度更新
    dz2 = -2 * (o2 - y)  # 输出误差 (o2 - y)**2 的导数
    dz1 = backprop(dz2, l2, o1)
    _ = backprop(dz1, l1, x)

# 画一个训练后的图，对比上文中有数值问题的线
draw_line(x, predict(x)[-1])
draw_scatter(x, y)

plt.show()

