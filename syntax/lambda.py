# lambda

y = lambda a: a * 2  # 인수(parameter) a를 받아서 2를 곱한 값을 반환
print(y(5))


# parameter가 여러개인 lambda 함수
print("---------parameter가 여러개인 lambda 함수----------")

z = lambda a, b: a * b
print(z(4, 5))


# lambda 함수를 다른 함수에 사용
print("---------lambda 함수를 다른 함수에 사용----------")


def my_function(n):
    return lambda a: a * n


mf1 = my_function(2)
print(mf1(5))


# filtering을 사용한 lambda
print("---------filtering을 사용한 lambda----------")

myList = list(filter(lambda x: x % 2, range(10)))
print(myList)
