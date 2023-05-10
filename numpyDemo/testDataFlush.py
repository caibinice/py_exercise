import numpy as np

raw_data = [
    ["Name", "StudentID", "Age", "AttendClass", "Score"],
    ["小明", 20131, 10, 1, 67],
    ["小花", 20132, 11, 1, 88],
    ["小菜", 20133, None, 1, "98"],
    ["小七", 20134, 8, 1, 110],
    ["花菜", 20134, 98, 0, None],
    ["刘欣", 20136, 12, 0, 12]
]

data = np.array(raw_data)
# print(data)

# test1 = np.array([1,2,3])
# test2 = np.array([1.1,2.3,3.4])
# test3 = np.array([1,2,3], dtype=np.float64)
# print("test1.dtype", test1.dtype)
# print("test2.dtype", test2.dtype)
# print("test3.dtype", test3.dtype)
#
# print("test2 > 2 ", test2 > 2)
# print("data > 2", data > 2)  # 这里会报错


data_process = []
for i in range(len(raw_data)):
    if i == 0:
        continue  # 不要首行字符串
    # 去掉首列名字
    data_process.append(raw_data[i][1:])
data = np.array(data_process, dtype=np.float64)
# print("data.dtype", data.dtype)
# print(data)

# # 查找是否有重复的数据，发现学生id重复了
# sid = data[:, 0]
# print(sid)
# unique, counts = np.unique(sid, return_counts=True)
# print(unique)
# print(counts)
#
# print(unique[counts > 1])
data[4, 0] = 20135

# 将没有记录(nan)或者取值范围异常(>=20岁)的年龄替换为其他列数据的平均年龄
# ~ 表示 True/False 对调，& 就是逐个做 Python and 的运算
normal_age_mask = ~np.isnan(data[:, 1]) & (data[:, 1] < 20)
print("是否为正常年龄normal_age_mask:", normal_age_mask)

normal_age_mean = data[normal_age_mask, 1].mean()
print("normal_age_mean:", normal_age_mean)

data[~normal_age_mask, 1] = normal_age_mean
# print("ages:", data[:, 1])

# 未上过课的学生总成绩应该为nan,先找到所有没上课的
normal_class = ~np.isnan(data[:, 2]) & (data[:, 2] > 0)
print("上过课的判断normal_class:", normal_class)

data[~normal_class, 3] = np.nan
# 超过 100 分和低于 0 分的都处理一下
data[:, 3] = np.clip(data[:, 3], 0, 100)
print("scores:", data[:, 2:4])
