import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.DataFrame([[1, None],[np.nan, 4]])
# print(df)
#
# print(df.isna())
# print(df.notna())

# df = pd.DataFrame({
#     "a": [1, None, 1],
#     "b": [np.nan, 4, 4]
# })
# print("skipped NaN:\n", df.mean(axis=0))
# print("\n\nnot skipped:\n", df.mean(axis=0, skipna=False))

# 去掉NaN所在行/列
# df = pd.DataFrame({
#     "a": [1, None, 3],
#     "b": [4, 5, 6]
# })
# print(df)
# print(df.dropna(axis=0))
# print(df.dropna(axis=1))

# 替换NaN
# 使用所在列平均值
# df = pd.DataFrame({
#     "a": [1, None, 3],
#     "b": [4, 5, 6]
# })
# a_mean = df["a"].mean()
# new_col = df["a"].fillna(a_mean)
# df["a"] = new_col
# print(df)

# 使用所在行另一列的值除以某个系数
# df = pd.DataFrame({
#     "a": [1, None, 3, None],
#     "b": [4, 8, 12, 12]
# })
# print(df)
# a_nan = df["a"].isna()
# a_new_value = df["b"][a_nan] / 4
# new_col = df["a"].fillna(a_new_value)
# df["a"] = new_col
# print(df)

# df = pd.DataFrame({
#     "a": [1, None, 3, None],
#     "b": [4, 8, 12, 12]
# })
# print(df)
# a_nan = df["a"].isna()
# df.loc[a_nan, "a"] = df["b"][a_nan] / 4
# print(df)

df = pd.DataFrame({
    "a": [1, 1, 2, 1, 2, 40, 1, 2, 1],
})
# df.plot()
df["a"] = df["a"].clip(lower=0, upper=3)
df.plot()









plt.show()








