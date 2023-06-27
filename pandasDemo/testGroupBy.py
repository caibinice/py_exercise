import pandas as pd
import numpy as np

# df = pd.DataFrame(
#     [
#         ("小红", "哈利波特", 80),
#         ("小明", "蜘蛛侠", 72),
#         ("小红", "雷神", 83),
#         ("小红", "蜘蛛侠", 45),
#         ("小明", "超人", 57),
#     ],
#     columns=("人", "人物", "评价"),
# )
# print(df)
# grouped = df.groupby("人")
# print(grouped)
#
# print(grouped.groups)
#
# print(df.iloc[grouped.groups["小红"]])
# print(grouped.get_group("小红"))


# print(grouped.first())
# print(grouped.last())
# print(grouped.sum())
# print(grouped.mean(numeric_only=True))


# for name, group in grouped:
#     print("name:", name)
#     print(group)

df = pd.DataFrame(
    [
        ("小红", "哈利波特", 80),
        ("小明", "蜘蛛侠", 72),
        ("小红", "雷神", 83),
        ("小红", "雷神", 90),
        ("小红", "蜘蛛侠", 45),
        ("小明", "超人", 57),
    ],
    columns=("人", "人物", "评价"),
)
print(df)

print(df.groupby(["人", "人物"]).get_group(("小红", "雷神")))
grouped = df.groupby("人")
print(grouped.aggregate(np.sum))
print(grouped["评价"].agg([np.sum, np.mean, np.std]))


print(grouped["评价"].agg(
    [np.sum, np.mean, np.std]
).rename(columns={
    "sum": "合",
    "mean": "均值",
    "std": "标准差"
}))

