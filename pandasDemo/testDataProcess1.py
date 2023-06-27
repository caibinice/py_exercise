import os
import pandas as pd
import matplotlib.pyplot as plt
# print(os.listdir("data"))

df = pd.read_csv("data/day_wise.csv")
# print(df.head())
#
#
#
# print("日期列表摘取：", df["Date"][:4])
# print(
#     "日期->索引转换：\n",
#     df[df["Date"] == "2020-02-03"]
# )


confirmed0124 = df.loc[df["Date"] == "2020-01-24", "Confirmed"]
# print(confirmed0124)
print("截止 1 月 24 日的累积确诊数：", confirmed0124.values)

result = df.loc[df["Date"] == "2020-07-23", "New deaths"]
print("截止 7 月 23 日的新增死亡数：", result.values)

date = pd.to_datetime(df["Date"])
date_range = (date >= "2020-01-25") & (date <= "2020-07-22")
new_cases = df.loc[date_range, "New cases"]
overall = new_cases.sum()
print("从 1 月 25 日到 7 月 22 日，一共增长了多少确诊病例：", overall)

confirmed = df.loc[:, "Confirmed"]
conf_0722 = confirmed.loc[df["Date"] == "2020-07-22"].values
conf_0125 = confirmed.loc[df["Date"] == "2020-01-25"].values

overall2 = conf_0722 - conf_0125
print("共新增：", overall2)

confirmed = df["Confirmed"]
new_cases = df["New cases"]
idx_0722 = df.loc[df["Date"] == "2020-07-22"].index.item()
idx_0125 = df.loc[df["Date"] == "2020-01-25"].index.item()

# for i in range(idx_0125, idx_0722+1):
#     diff = new_cases.iloc[i] - (confirmed.iloc[i] - confirmed.iloc[i-1])
#     if diff != 0:
#         print("date index:", i, ";差异：", diff)

# 每天新增确诊数和新恢复数的比例？平均比例，标准差各是多少？
ratio = df["New cases"] / df["New recovered"]
# print("比例样本：", ratio[:5])
# print(df.loc[0, "New cases"])
# print(df.loc[0, "New recovered"])

not_zero_mask = df["New recovered"] != 0
ratio = df.loc[not_zero_mask, "New cases"] / df.loc[not_zero_mask, "New recovered"]

# 平均比例, 标准差
ratio_mean = ratio.mean()
ratio_std = ratio.std()
print("平均比例：", ratio_mean, "；标准差：", ratio_std)

# df["New cases"].plot()
# print(df.loc[50, "Date"])

df["Deaths / 100 Cases"].plot()



















plt.show()