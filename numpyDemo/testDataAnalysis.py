import numpy as np
import matplotlib.pyplot as plt


def draw_line(d):
    plt.figure()
    plt.plot(d)
    plt.show()


with open("covid19_day_wise.csv", "r", encoding="utf-8") as f:
    data = f.readlines()

covid = {
    "date": [],
    "data": [],
    "header": [h for h in data[0].strip().split(",")[1:]]
}
for row in data[1:]:
    split_row = row.strip().split(",")
    covid["date"].append(split_row[0])
    covid["data"].append([float(n) for n in split_row[1:]])

# 数据概览
# print(covid["header"])
# print(covid["date"])
# print(covid["data"][:5]) # 数据太多了，我先打 5 行
# print(covid["data"]) # 如果你实在想看全部，就执行这一行

#  转为numpy列表
data = np.array(covid["data"])

# 获取 2020 年 2 月 3 日的所有数据
# print("日期列表摘取：", covid["date"][:4])
# date_idx = covid["date"].index("2020-02-03")
# print("日期->索引转换：", date_idx)
#
# for header, number in zip(covid["header"], data[date_idx]):
#     print(header, ":", number)


# 2020 年 1 月 24 日之前的累积确诊病例有多少个？
# date_idx = covid["date"].index("2020-01-24")
# header_idx = covid["header"].index("Confirmed")
# count = data[date_idx, header_idx]
# # count = data[date_idx][header_idx]
# print(f"2020 年 1 月 24 日之前的累积确诊病例有{count}个")


# 2020 年 7 月 23 日的新增死亡数是多少？
# date_idx = covid["date"].index("2020-07-23")
# header_idx = covid["header"].index("New deaths")
# count = data[date_idx, header_idx]
# # count = data[date_idx][header_idx]
# print(f"2020 年 7 月 23 日的新增死亡数是{count}个")


# 从 1 月 25 日到 7 月 22 日，一共增长了多少确诊病例？
# header_idx = covid["header"].index("New cases")
# date_idx_start = covid["date"].index("2020-01-25")
# date_idx_end = covid["date"].index("2020-07-22")
# count = 0.0
# for i in range(date_idx_start, date_idx_end + 1):
#     count += data[i, header_idx]
# print(f"从 1 月 25 日到 7 月 22 日，一共增长了{count}个确诊病例")
#
# row1_idx = covid["date"].index("2020-01-25")
# row2_idx = covid["date"].index("2020-07-22")
# new_cases_idx = covid["header"].index("New cases")
# new_cases = data[row1_idx: row2_idx+1, new_cases_idx]
# overall = new_cases.sum()
# print("共新增：", overall)


# # 每天新增确诊数和新恢复数的比例？平均比例，标准差各是多少？
# header_idx_new_cases = covid["header"].index("New cases")
# header_idx_new_recovered = covid["header"].index("New recovered")
# not_zero_mask = data[:, header_idx_new_recovered] != 0
# # print(not_zero_mask)
# data_ratio = data[not_zero_mask, header_idx_new_cases] / data[not_zero_mask, header_idx_new_recovered]
# print(data_ratio[:5])
#
# # 平均比例, 标准差
# ratio_mean = data_ratio.mean()
# ratio_std = data_ratio.std()
# print("平均比例：", ratio_mean, "；标准差：", ratio_std)


# 画图展示新增确诊的变化曲线
# new_cases_idx = covid["header"].index("New cases")
# draw_line(data[:, new_cases_idx])

# 画图展示死亡率的变化曲线
death_idx = covid["header"].index("Deaths / 100 Cases")
draw_line(data[:, death_idx])
