import numpy as np

# a = np.array([1, 2, 3, 4, 5, 6])
# a_2d = a[np.newaxis, :]
# # print(a.shape, a_2d.shape)
#
# a = np.array([1,2,3,4,5,6])
# a_none = a[:, None]
# a_expand = np.expand_dims(a, axis=1)
# print(a_none.shape, a_expand.shape)
# print(a_none)
# print(a_expand)
#
# a_squeeze = np.squeeze(a_expand)
# a_squeeze_axis = a_expand.squeeze(axis=1)
# print(a_squeeze)
# print(a_squeeze_axis)
# print(a_squeeze.shape)
# print(a_squeeze_axis.shape)

# a = np.array([1, 2, 3, 4, 5, 6])
# a1 = a.reshape([2, 3])
# a2 = a.reshape([3, 1, 2])
# print("a1 shape:", a1.shape)
# print(a1)
# print("a2 shape:", a2.shape)
# print(a2)


# a = np.array([1, 2, 3, 4, 5, 6]).reshape([2, 3])
# aT1 = a.T
# aT2 = np.transpose(a)
# print(a)
# print(aT1)
# print(aT2)

# feature_a = np.array([1, 2, 3, 4, 5, 6])
# feature_b = np.array([11, 22, 33, 44, 55, 66])
# c_stack = np.column_stack([feature_a, feature_b])
# print(np.shape(c_stack))
#
# sample_a = np.array([0, 1.1])
# sample_b = np.array([1, 2.2])
# c_stack = np.row_stack([sample_a, sample_b])
# print(np.shape(c_stack))
# print(c_stack)

# feature_a = np.array([1,2,3,4,5,6])[:, None]
# feature_b = np.array([11,22,33,44,55,66])[:, None]
# print(feature_a)
# print(feature_b)
# c_stack = np.hstack([feature_a, feature_b])
# print(c_stack)
#
# sample_a = np.array([0, 1.1])[None, :]
# sample_b = np.array([1, 2.2])[None, :]
# c_stack = np.vstack([sample_a, sample_b])
# print(sample_a)
# print(sample_b)
# print(c_stack)


# a = np.array([
#     [1, 2],
#     [3, 4]
# ])
# b = np.array([
#     [5, 6],
#     [7, 8]
# ])
#
# print(np.concatenate([a, b], axis=0))
# print(np.concatenate([a, b], axis=1))

# a = np.array(
# [[ 1, 11, 2, 22],
#  [ 3, 33, 4, 44],
#  [ 5, 55, 6, 66],
#  [ 7, 77, 8, 88]]
# )
#  vsplit 水平切分  hsplit 垂直拆分
# print(np.vsplit(a, indices_or_sections=2))  # 分成两段
# print(np.vsplit(a, indices_or_sections=[2,3]))  # 分片成 [:2]，[2:3], [3:]


a = np.array(
[[ 1, 11, 2, 22],
 [ 3, 33, 4, 44],
 [ 5, 55, 6, 66],
 [ 7, 77, 8, 88]]
)
print(np.split(a, indices_or_sections=2, axis=0))  # 水平分成两段（维持第一维度不变）
print(np.split(a, indices_or_sections=[2,3], axis=1))  # 在第二维度（垂直），分片成 [:2]，[2:3]，[3:]


