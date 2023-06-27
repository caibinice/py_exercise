import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2
# plt.figure()
# plt.plot(x, y)
# plt.show()

plt.figure(num=3, figsize=(8, 5),)
l1, = plt.plot(x, y1, label='linear line')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')

plt.xlim((-3, 3))
plt.ylim((-6, 8))
# plt.xlabel('I am x')
# plt.ylabel('I am y')
new_ticks = np.linspace(-3, 3, 7)
print(new_ticks)
plt.xticks(new_ticks)
# plt.yticks([-2, -1.4, -1, 1.4, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('blue')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# plt.legend(loc='upper right')
plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')
# 'best': 0,
# 'upper right': 1,
# 'upper left': 2,
# 'lower left': 3,
# 'lower right': 4,
# 'right': 5,
# 'center left': 6,
# 'center right': 7,
# 'lower center': 8,
# 'upper center': 9,
# 'center': 10,



#  添加标注和注释
x0 = 1
y0 = 2*x0 + 1
plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)
# set dot styles
plt.scatter([x0, ], [y0, ], s=50, color='b')
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

plt.text(-3, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})

# 设置坐标轴透明度
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    # 在 plt 2.0.2 或更高的版本中, 设置 zorder 给 plot 在 z 轴方向排序
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7, zorder=2))

plt.show()


