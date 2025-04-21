import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 忽略部分版本警告
warnings.filterwarnings('ignore')
# 设置sns样式
sns.set(style='white', context='notebook', palette='muted')

df = pd.read_csv("https://blog.caiyongji.com/assets/penguins_size.csv")
print(df.shape)
df = df.dropna()
print(df.head())

sns.pairplot(df, hue='species')
plt.show()

X = pd.get_dummies(df.drop('species', axis=1), drop_first=True)
y = df['species']
print(X.head())


