import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 忽略部分版本警告
warnings.filterwarnings('ignore')

# 设置sns样式
sns.set(style='white', context='notebook', palette='muted')

# 导入数据
train = pd.read_csv('./train.csv')
test = pd.read_csv('./test.csv')

# 合并数据集
full = pd.concat([train, test], ignore_index=True)

print(test.head())
print(test.describe())


# 数据前5行和数据大致描述
# print(full.head(5))
# print(full.describe())

# 计算不同类型embarked的乘客，其生存率为多少
# S:南安普顿港southampton;Q:皇后镇 Queentown;C:瑟堡 Cherbourg
print('Embarked为"S"的乘客，其生存率为%.2f' % full['Survived'][full['Embarked'] == 'S'].value_counts(normalize=True)[1])
print('Embarked为"C"的乘客，其生存率为%.2f' % full['Survived'][full['Embarked'] == 'C'].value_counts(normalize=True)[1])
print('Embarked为"Q"的乘客，其生存率为%.2f' % full['Survived'][full['Embarked'] == 'Q'].value_counts(normalize=True)[1])


# sns.catplot(x='Pclass', col='Embarked', data=train, kind='count', height=3)

# SibSp与Survived：当乘客同行的同辈数量适中时生存率较高
# sns.barplot(data=train, x='SibSp', y='Survived')

# Pclass与Survived：乘客客舱等级越高，生存率越高
# sns.barplot(data=train, x='Pclass', y='Survived')

# Sex与Survived：女性的生存率远高于男性
# sns.barplot(data=train, x='Sex', y='Survived')

# sns.barplot(data=train, x='Parch', y='Survived')


ageFacet = sns.FacetGrid(train, hue='Survived', aspect=3)  # 创建坐标轴
ageFacet.map(sns.kdeplot, 'Age', shade=True)  # 作图，选择图形类型
ageFacet.set(xlim=(0, train['Age'].max()))  # 其他信息：坐标轴范围、标签等
ageFacet.add_legend()


plt.show()

