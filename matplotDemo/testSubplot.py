import matplotlib.pyplot as plt

plt.figure()

# 均匀分割
# plt.subplot(2, 2, 1)
# plt.plot([0, 1], [0, 1])
#
# plt.subplot(2,2,2)
# plt.plot([0,1],[0,2])
#
# plt.subplot(223)
# plt.plot([0,1],[0,3])
#
# plt.subplot(224)
# plt.plot([0,1],[0,4])

# 不均匀分割 第一行1个图，第二行三个图
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])

plt.subplot(2,3,4)
plt.plot([0,1],[0,2])

plt.subplot(235)
plt.plot([0,1],[0,3])

plt.subplot(236)
plt.plot([0,1],[0,4])

plt.show()  # 展示
