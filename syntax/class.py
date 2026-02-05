# class myClass:
#     x = 5


# p1 = myClass()
# print(p1.x)


# 생성자: class 생성되는 객체의 초기화를 담당하는 함수
class Person:
    # self는 객체 자신(defalut 값)
    def __init__(self, name, age):
        self.name = name
        self.age = age


p2 = Person("marshall", 20)
print(p2.name)
print(p2.age)
