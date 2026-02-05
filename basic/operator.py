# 산술 연산자 : +, -, *, /, %, **(제곱), //(버림 나눗셈)

x = 5
y = 10
print(x + y)  # 15
print(x - y)  # -5
print(x * y)  # 50
print(x / y)  # 0.5
print(x % y)  # 5
print(y % x)  # 0
print(x**y)  # 9765625
print(2**3)  # 8

# // : 버림 나눗셈
print(10 // 3)  # 3 : 10을 3으로 나눈 몫에서 소수점 이하를 버림
print(10 % 3)  # 1
print(10 / 3)  # 3.3333333333333335

# 대입 연산자 : =, +=, -=, *=, /=, %=, **=, //=
x = 10
x += 5  # x = x + 5
print(x)  # 15

x -= 5  # x = x - 5
print(x)  # 10

x *= 5  # x = x * 5
print(x)  # 50

x /= 5  # x = x / 5
print(x)  # 10.0

x %= 3  # x = x % 3
print(x)  # 1.0

x **= 3  # x = x ** 3
print(x)  # 1.0

x //= 3  # x = x // 3
print(x)  # 0.0

# 비교 연산자 : ==, !=, >, <, >=, <=
x = 10
y = 5
print(x == y)  # False
print(x != y)  # True
print(x > y)  # True
print(x < y)  # False
print(x >= y)  # True
print(x <= y)  # False

# 논리 연산자 : and, or, not
x = 10
y = 5
print(x > 3 and y < 10)  # True
print(x > 3 and y > 10)  # False
print(x > 3 or y > 10)  # True
print(x < 3 or y > 10)  # False
print(not x > 3)  # False
print(not y > 3)  # True
