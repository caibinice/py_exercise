# def inner_pre_fn(name):
#     print(name+"say I'm in_pre")
#
# def inner_post_fn(name):
#     print(name+"say I'm in_post")
#
# def outer_fn(name):
#     inner_pre_fn(name)
#     print(name+"say I'm out")
#     inner_post_fn(name)
#
# outer_fn("mofanpy")

# def decorator(fn, name):
#     print(name+"say I'm in")    # 这是我的前处理
#     return fn(name)
#
# def outer_fn(name):
#     print(name+"say I'm out")
#
# decorator(outer_fn, "mofanpy")


# def decorator(fn):
#     def wrapper(name):
#         print(name+"say I'm in")    # 这是我的前处理
#         return fn(name)
#     return wrapper
#
# @decorator
# def outer_fn(name):
#     print(name+"say I'm out")
#
# outer_fn("mofanpy")


# def decoratorA(fn):
#     def wrapper(name):
#         print(name+"say I'm in_pre")    # 这是我的前处理
#         res = fn(name)
#         print(name+"say I'm in_post")   # 这是我的后处理
#         return res + "_wrapper_fn"
#     return wrapper
#
# @decoratorA
# def outer_fn(name):
#     print(name+"say I'm out")
#     return name + "_outer_fn"
#
# print(outer_fn("mofanpy"))


def authorization(fn):
    def check_and_do(name):
        if name != "mofanpy":   # 鉴权
            print(name + " has no right!")
            return
        res = fn(name)
        return res
    return check_and_do

@authorization
def outer1(name):
    print(name+" outer1")

@authorization
def outer2(name):
    print(name+" outer2")

@authorization
def outer3(name):
    print(name+" outer3")

outer1("mofanpy")
outer2("morgan")
outer3("mofanpy")


