# if 조건문
a = 300
b = 200
c = 100

# if a < b:
#     print("a가 b보다 작습니다.")
# elif a == b:
#     print("a와 b가 같습니다.")
# else:
#     print("a가 b보다 큽니다.")


# if 축약형
# if a < b:
#     print("a가 b보다 작습니다.")
# print("a가 b보다 작습니다.") if a < b else print("a가 b보다 큽니다.")
# print("a") if a > b else print("=") if a == b else print("b")


# 논리 연산: &&(and), ||(or), !(not)
# if a > b and a > c:
#     print("a is greater than b and c")

# if a > b or a < c:
#     print("a is greater than b or a is less than c")

# if not (b > a):
#     print("b is not greater than a")


# if nesting
x = 24

if x > 5:
    print("x is greater than 5")
    if x > 20:
        print("x is greater than 20")
    else:
        print("x is less than 20")
else:
    print("x is less than 5")
