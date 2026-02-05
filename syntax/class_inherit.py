# class 기능 상속 (확장)


class Person:
    # self는 객체 자신(defalut 값)
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

    # //! [Original Code] 클래스 정의 내부(들여쓰기 된 상태)에서 호출하여 NameError 발생
    # x = Person("marshall", "han")
    # x.printname()


# //* [Modified Code] 들여쓰기를 제거하여 클래스 정의가 끝난 후 실행되도록 수정
x = Person("marshall", "han")
x.printname()


class Student(Person):  # Person 클래스 기능을 상속받음
    def __init__(self, fname, lname, year):
        # super(): 부모 클래스의 생성자 호출 함수
        super().__init__(fname, lname)  # self를 제외한 부모 클래스의 생성자 호출
        self.graduationyear = year

    def printname(self):
        print(self.firstname, self.lastname, self.graduationyear)


x = Student("marshall", "han", 2020)
x.printname()
