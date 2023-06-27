import os
import pandas as pd
import matplotlib.pyplot as plt

os.listdir("data")

path = "data/iris.csv"
columns = ["sepal length", "sepal width", "petal length", "petal width", "class"]
df = pd.read_csv("data/iris.csv", names=columns)
# print(df)
# # print(df.isna())
# print(df.isna().any())
#
# print(df.loc[pd.isna(df["petal width"])])
df1 = df.dropna(axis=0, how="any")
# print(df1.isna().any())
# df1.plot()

index = df1[df1["sepal length"]<0].index
df2 = df1.drop(index)
# df2["sepal length"].plot()

# df2["sepal width"].plot()
index = df2[df2["sepal width"]>5].index
df2 = df2.drop(index)
# df2.plot()

index = df2[df2["petal width"]>5].index
df2 = df2.drop(index)
# df2.plot()



df3 = df2.sample(frac=1)
# print(df3)
total_data = len(df2)
n_train = int(total_data * 0.8)

train_data = df3.iloc[:n_train]
test_data = df3.iloc[n_train:]
# print(test_data)

print(train_data.loc[:, "class"])

def get_xy(df):
    return df[["sepal length", "sepal width", "petal length", "petal width"]], df[["class"]]

train_x, train_y = get_xy(train_data)
print(train_x.head())
print(train_y.head())

test_x, test_y = get_xy(test_data)
print(test_x.head())
print(test_y.head())

train_x_array, train_y_array = train_x.values, train_y.values
print(train_x_array[:3])



plt.show()

