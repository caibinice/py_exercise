import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython import display

# display.set_matplotlib_formats('svg')
# Alternative to set svg for newer versions

# 设置图片svg格式
import matplotlib_inline

matplotlib_inline.backend_inline.set_matplotlib_formats('svg')

# 读取数据，可直接读取zip压缩文件
# data = pd.read_csv('data/house_sales.zip')
data = pd.read_feather('data/house_sales.ftr')

# 查看数据大小，以及大致包含的信息
print(data.shape)
print(data.head(5))

# 丢弃掉缺失信息>30%的列
null_sum = data.isnull().sum()
print(data.columns[null_sum < len(data) * 0.3])  # columns will keep
data.drop(columns=data.columns[null_sum > len(data) * 0.3], inplace=True)

# 查看剩下列的数据类型，根据其所代表的具体信息转换数据类型
print(data.dtypes)

# Convert currency from string format such as $1,000,000 to float.
# 先去掉美元符号'$'和空值符号'-'，然后将空字符串转换为np.nan空值，然后再统一转float
currency = ['Sold Price', 'Listed Price', 'Tax assessed value', 'Annual tax amount']
for c in currency:
    data[c] = data[c].replace(
        r'[$,-]', '', regex=True).replace(
        r'^\s*$', np.nan, regex=True).astype(float)

# convert areas from string format such as 1000 sqft and 1 Acres to float as well.
areas = ['Total interior livable area', 'Lot size']
for c in areas:
    acres = data[c].str.contains('Acres') == True
    col = data[c].replace(r'\b sqft\b|\b Acres\b|\b,\b', '', regex=True).astype(float)
    col[acres] *= 43560
    data[c] = col

# Now we can check values of the numerical columns.
# You could see the min and max values for several columns do not make sense.
# 查看数据分布，针对性地处理掉一些不合理的异常值，如小于10或者超过4位数的面积
print(data.describe())

# We filter out houses whose living areas are too small or too hard to simplify the visualization later.
abnormal = (data[areas[1]] < 10) | (data[areas[1]] > 1e4)
data = data[~abnormal]
print(sum(abnormal))

# Let's check the histogram of the 'Sold Price', which is the target we want to predict.
# 查看房价的指数分布
# ax = sns.histplot(np.log10(data['Sold Price']))
# ax.set_xlim([3, 8])
# ax.set_xticks(range(3, 9))
# ax.set_xticklabels(['%.0e' % a for a in 10 ** ax.get_xticks()])


# A house has different types. Here are the top types:
# 查看出现数量最多的房型
print(data['Type'].value_counts()[0:20])

# Price density for different house types.
# 展示数量最多的几种房型的价格密度分布
# types = data['Type'].isin(['SingleFamily', 'Condo', 'MultiFamily', 'Townhouse'])
# sns.displot(pd.DataFrame({'Sold Price': np.log10(data[types]['Sold Price']),
#                           'Type': data[types]['Type']}),
#             x='Sold Price', hue='Type', kind='kde')


# Another important measurement is the sale price per living sqft.
# Let's check the differences between different house types.
# 查看不同房子类型的每平米价格 中间横线代表均值
data['Price per living sqft'] = data['Sold Price'] / data['Total interior livable area']
# ax = sns.boxplot(x='Type', y='Price per living sqft', data=data[types], fliersize=0)
# ax.set_ylim([0, 2000])

# We know the location affect the price.
# Let's check the price for the top 20 zip codes.
# 不同的邮政编码（具体地区）的房屋均价分布
# d = data[data['Zip'].isin(data['Zip'].value_counts()[:20].keys())]
# ax = sns.boxplot(x='Zip', y='Price per living sqft', data=d, fliersize=0)
# ax.set_ylim([0, 2000])
# ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

# Last, we visualize the correlation matrix of several columns.
# 查看各种价格之间的相关关系，即协方差矩阵，比如：Sold Price 和 Annual tax amount协方差达到0.5，说明卖出价格和每年房产税的正相关性很高，即年房产税高，则卖出价格高
# 再比如：Elementary School Score 和High School Score 协方差达到0.4，说明房屋地段的小学分数和高中分数呈现很高的正相关性，即小学分数高的高中分数也高
_, ax = plt.subplots(figsize=(6, 6))
columns = ['Sold Price', 'Listed Price', 'Annual tax amount', 'Price per living sqft', 'Elementary School Score',
           'High School Score']
sns.heatmap(data[columns].corr(), annot=True, cmap='RdYlGn', ax=ax)

plt.show()
