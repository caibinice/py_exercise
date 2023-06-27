import pandas as pd



df1 = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
}, index=[0, 1, 2, 3],)


df2 = pd.DataFrame({
    "A": ["A4", "A5", "A6", "A7"],
    "B": ["B4", "B5", "B6", "B7"],
    "C": ["C4", "C5", "C6", "C7"],
    "D": ["D4", "D5", "D6", "D7"],
}, index=[4, 5, 6, 7],)


df3 = pd.DataFrame({
    "A": ["A8", "A9", "A10", "A11"],
    "B": ["B8", "B9", "B10", "B11"],
    "C": ["C8", "C9", "C10", "C11"],
    "D": ["D8", "D9", "D10", "D11"],
}, index=[8, 9, 10, 11],)


# all_classes = pd.concat(
#     [df1, df2, df3],
#     keys=["x", "y", "z"])
# print(all_classes)
#
# print(all_classes.loc["y"])


df4 = pd.DataFrame({
    "B": ["B2", "B3", "B6", "B7"],
    "D": ["D2", "D3", "D6", "D7"],
    "F": ["F2", "F3", "F6", "F7"],
}, index=[2, 3, 6, 7],)

# print(pd.concat([df1, df4], axis=1))
#
# print(pd.concat([df1, df4], axis=1, join="inner"))

# print(pd.concat(
#     [df1, df4],
#     ignore_index=True,
#     sort=False))
new_col = pd.Series(
    ["X0", "X1", "X2", "X3"], name="X")

# print(pd.concat([df1, new_col], axis=1))
new_row = pd.Series(
    ["X0", "X1", "X2", "X3"],
    index=["A", "B", "C", "D"])
# print(pd.concat(
#     [df1, new_row.to_frame().T],
#     ignore_index=True))

# print(df1._append(new_row, ignore_index=True))


left = pd.DataFrame({
    "key": ["K0", "K1", "K2", "K3"],
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
})


right = pd.DataFrame({
    "key": ["K0", "K1", "K2", "K3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
})


# print(pd.merge(left, right, on="key"))

left = pd.DataFrame({
    "key1": ["K0", "K0", "K1", "K2"],
    "key2": ["K0", "K1", "K0", "K1"],
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
})


right = pd.DataFrame({
    "key1": ["K0", "K1", "K1", "K2"],
    "key2": ["K0", "K0", "K0", "K0"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
})


# print(pd.merge(left, right, on=["key1", "key2"]))
#
#
#
# print(pd.merge(left, right, how="left", on=["key1", "key2"]))


left = pd.DataFrame({
    "A": ["A0", "A1", "A2"],
    "B": ["B0", "B1", "B2"]
}, index=["K0", "K1", "K2"])


right = pd.DataFrame({
    "C": ["C0", "C2", "C3"],
    "D": ["D0", "D2", "D3"]
}, index=["K0", "K2", "K3"])

# print(left.join(right))


left = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "key": ["K0", "K1", "K0", "K1"],
})


right = pd.DataFrame({
    "C": ["C0", "C1"],
    "D": ["D0", "D1"]
}, index=["K0", "K1"])

print(left.join(right, on="key"))
