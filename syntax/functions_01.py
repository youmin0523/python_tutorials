# function: def 키워드 사용


def add(a, b):
    return a + b


print(add(1, 3))


# arbitary arguments
print("---------arbitary arguments----------")


def arb_func(*args):
    print("age is {}, name is {}".format(args[0], args[1]))
    print(args)
    print(type(args))


arb_func("20", "marshall")


# keyword arguments
print("---------keyword arguments----------")


def key_arg_func(**kwargs):
    print("age is {}, name is {}".format(kwargs["age"], kwargs["name"]))
    print(kwargs)
    print(type(kwargs))


key_arg_func(age="20", name="marshall")
