import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# plt.figure()
# 使用plt.subplot2grid来创建第1个小图, (3,3)表示将整个图像窗口分成3行3列,
# (0,0)表示从第0行第0列开始作图，colspan=3表示列的跨度为3, rowspan=1表示行的跨度为1.
# colspan和rowspan缺省, 默认跨度为1.
# ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
# ax1.plot([1, 2], [1, 2])    # 画小图
# ax1.set_title('ax1_title')  # 设置小图的标题
#
# ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
# ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
# ax4 = plt.subplot2grid((3, 3), (2, 0))
# ax5 = plt.subplot2grid((3, 3), (2, 1))
#
# ax4.scatter([1, 2], [2, 2])
# ax4.set_xlabel('ax4_x')
# ax4.set_ylabel('ax4_y')

# gridspec¶
# plt.figure()
# gs = gridspec.GridSpec(3, 3)
# # 使用plt.subplot来作图, gs[0, :]表示这个图占第0行和所有列,
# # gs[1, :2]表示这个图占第1行和第2列前的所有列, gs[1:, 2]表示这个图占第1行后的所有行和第2列,
# # gs[-1, 0]表示这个图占倒数第1行和第0列, gs[-1, -2]表示这个图占倒数第1行和倒数第2列.
# ax6 = plt.subplot(gs[0, :])
# ax7 = plt.subplot(gs[1, :2])
# ax8 = plt.subplot(gs[1:, 2])
# ax9 = plt.subplot(gs[-1, 0])
# ax10 = plt.subplot(gs[-1, -2])
#
#
# ax9.plot([1, 2], [1, 2])


# 使用plt.subplots建立一个2行2列的图像窗口，sharex=True表示共享x轴坐标, sharey=True表示共享y轴坐标.
# ((ax11, ax12), (ax13, ax14))表示第1行从左至右依次放ax11和ax12, 第2行从左至右依次放ax13和ax14.
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax13.scatter([1,2], [1,2])
plt.tight_layout() # 紧凑显示

plt.show()

