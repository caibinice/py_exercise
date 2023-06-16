import pandas as pd

# py_s = "A,B,C,Aaba,Baca,CABA,dog,cat"
# pd_s = pd.Series(
#     ["A", "B", "C", "Aaba", "Baca", "CABA", "dog", "cat"],
#     dtype="string")
# print("python:\n", py_s.upper())
# print("\npandas:\n", pd_s.str.upper())
# pd_not_s = pd.Series(
#     ["A", "B", "C", "Aaba", "Baca", "CABA", "dog", "cat"],
# )
# print("pd_not_s type:", pd_not_s.dtype)
# pd_s = pd_not_s.astype("string")
# print("pd_s type:", pd_s.dtype)
# print("python lower:\n", py_s.lower())
# print("\npandas lower:\n", pd_s.str.lower())
# print("python len:\n", [len(s) for s in py_s.split(",")])
# print("\npandas len:\n", pd_s.str.len())

# py_s = ["   jack", "jill ", "    jesse    ", "frank"]
# pd_s = pd.Series(py_s, dtype="string")
# print("python strip:\n", [s.strip() for s in py_s])
# print("\npandas strip:\n", pd_s.str.strip())
#
# print("\n\npython lstrip:\n", [s.lstrip() for s in py_s])
# print("\npandas lstrip:\n", pd_s.str.lstrip())
#
# print("\n\npython rstrip:\n", [s.rstrip() for s in py_s])
# print("\npandas rstrip:\n", pd_s.str.rstrip())

# py_s = ["a_b_c", "jill_jesse", "frank"]
# pd_s = pd.Series(py_s, dtype="string")
# print("python split:\n", [s.split("_") for s in py_s])
# print("\npandas split:\n", pd_s.str.split("_"))
# print(pd_s.str.split("_", expand=True))


# pd_df = pd.DataFrame([["a", "b"], ["C", "D"]])
# pd_df.iloc[0, :] = pd_df.iloc[0, :].str.upper()
# print(pd_df)

# pattern = r"[0-9][a-z]"
# s = pd.Series(["1", "1a", "11c", "abc"], dtype="string")
# print(s.str.contains(pattern))
# pattern1 = r"[0-9]+?[a-z]"
# print(s.str.match(pattern1))


py_s = ["1", "1a", "21c", "abc"]
pd_s = pd.Series(py_s, dtype="string")
# print("py_s replace '1' -> '9':\n", [s.replace("1", "9") for s in py_s])
#
# print("\n\npd_s replace '1' -> '9':\n", pd_s.str.replace("1", "9"))


# print("pd_s replace -> 'NUM':", pd_s.str.replace(r"[0-9]", "NUM", regex=True))

s = pd.Series(['a1', 'b2', 'c3'])
# print(s.str.extract(r"([ab])(\d)"))

s1 = pd.Series(["A", "B", "C", "D"], dtype="string")
s2 = pd.Series(["1", "2", "3", "4"], dtype="string")
print(s1.str.cat(s2))

