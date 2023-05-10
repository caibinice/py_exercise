# def add(a, b):
#     return a + b
#
#
# print(add(1, 2))
#
# add = lambda a, b: a + b
# print(add(1, 2))


# l = []
# for i in range(10):
#     l.append(i*2)
# print(l)
#
# l = [i*2 for i in range(10)]
# print(l)
#
# d = {"index"+str(i): i*2 for i in range(10)}
# print(d)


# done = False
# if done:
#     a = 1
# else:
#     a = 2
# print(a)
#
# done = False
# a = 1 if done else 2
# print(a)


# l = []
# for i in range(10):
#     if i % 2 == 0:
#         l.append(i * 2)
# print(l)

# 循环的简写
# ll = [i * 2 for i in range(10) if i % 2 == 0]
# print(ll)
# ll = {"index" + str(i): i * 2 for i in range(10) if i % 2 == 0}
# print(ll)
# print(ll.get("index2"))

# count = 0
# l = [11,22,33,44]
# for data in l:
#     if count == 2:
#         data += 11
#     l[count] = data
#     count += 1
# print(l)
#
# l = [11,22,33,44]
# for count, data in enumerate(l):
#     if count == 2:
#         data += 11
#     l[count] = data
# print(l)
#
#
# l = [11,22,33,44]
# d = {}
# for count, data in enumerate(l, start=5):
#     d[count] = data
# print(d)


# name = ["a", "b", "c"]
# score = [1, 2, 3]
# d = {}
# for i in range(3):
#     d[name[i]] = score[i]
# print(d)
#
# name = ["a", "b", "c"]
# score = [1,2,3]
# d = {}
# for n, s in zip(name, score):
#     d[n]=s
# print(d)
#
# name = ["a", "b", "c"]
# score = [1,2,3]
# bonus = [1,0,1]
# d = {}
# for n, s, b in zip(name, score, bonus):
#     d[n]=s+b
# print(d)

# l = [1,2,3]
# _l = []
# for i in range(len(l)):
#     _l.append(l[-i-1])
# print(_l)
#
# l = [1,2,3]
# _l = [l[-i-1] for i in range(len(l))]
# print(_l)
#
# l = [1,2,3]
# l.reverse()
# print(l)
#
# l = [1,2,3]
# for i in reversed(l):
#     print(i)
#
# l = [1,2,3]
# _l = l[::-1]
# print(l)
# print(_l)


# 浅拷贝和深拷贝
# l = [[1],[2],3]
# _l = l.copy()
# _l[0][0] = -1
# print(_l)
# print(l)
#
# from copy import deepcopy
# l = [[1],[2],3]
# _l = deepcopy(l)
# _l[0][0] = -1
# print(_l)
# print(l)




