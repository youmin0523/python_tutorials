# default parameter
print("---------default parameter----------")


def my_function(country="Korea"):
    print(f"I am from {country}")


my_function()
my_function("USA")


# collection parameter
print("---------collection parameter----------")


def my_function_01(param):
    for x in param:
        print(x)


my_function_01([1, 2, 3, 4])
my_function_01((1, 2, 3, 4))


# prevent defualt parameter
print("---------prevent defualt parameter----------")


def my_function_02(aaa, /):
    print(aaa)


my_function_02(1)


# keyword only pararmeter
print("---------keyword only pararmeter----------")


def my_function_03(*, bbb):
    print(bbb)


my_function_03(bbb=2)
