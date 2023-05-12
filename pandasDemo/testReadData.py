import pandas as pd
import os


# print(os.listdir("data"))
#
# df = pd.read_excel("data/体检数据.xlsx", index_col=0)
#
# print(df)
#
# df.loc[2, "体重"] = 1
# print(df)
# df.to_excel("data/体检数据_修改.xlsx")
#
# df1 = pd.read_excel("data/体检数据_修改.xlsx", index_col=0)
#
# print(df1)

# with open("data/体检数据.csv", "r", encoding="utf-8") as f:
#     print(f.read())
#
# df_csv = pd.read_csv("data/体检数据.csv", index_col=0)
# print(df_csv)

# with open("data/体检数据_sep.csv", "r", encoding="utf-8") as f:
#     print(f.read())
# df_csv = pd.read_csv("data/体检数据_sep.csv", index_col=0, sep="=")
# print(df_csv)

with open("data/体检数据_sep.txt", "r", encoding="utf-8") as f:
    print(f.read())
df_txt = pd.read_csv("data/体检数据_sep.txt", index_col=0, sep="=")
print(df_txt)