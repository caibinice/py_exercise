def my_func1(a):
    if a == 1:
        return 2
    elif a == -1:
        return 3
    else:
        return 1


def my_func2(b):
    if b != "yes":
        raise ValueError("you can only say yes!")
    else:
        return True
