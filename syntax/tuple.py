# 자료 묶음 문법 : List, (Tuple), Set, Dictionary
# Tuple
# 1. 값을 변경할 수 없다
# 2. 중복 데이터를 허용한다
# 3. 순서를 가지고 있다 (인덱스가 있다)
# 4. 소괄호를 사용한다 (생략 가능)
# 5. 모든 타입을 요소로 지정할 수 있다

print("---------tuple test----------")

a = ("사과", "복숭아", "사과", 1, True)
b = "apple"
c = "grape", "banana"

print(a)
print(b)
print(c)
print(type(a))  # tuple
print(type(b))  # tuple 데이터가 하나일 경우 str로 인식
print(type(c))  # tuple

# 요소의 접근
print("---------tuple 접근----------")
print(a[1])
print(a[1:3])

# 생성자로 튜플 생성
print("---------tuple 생성----------")
d = tuple((1, 2, "사과"))
print(d)

# if문으로 요소 체크
print("---------if문으로 요소 체크----------")
if "사과" in a:
    print(True)
    pass

# 요소의 변경 (리스트 형태로 변경한 후에 다시 튜플로 변환해야함)
print("---------요소의 변경----------")
print(a)
e = list(a)
e[1] = "포도"
print(e)

f = tuple(e)
print(f)

# tuple 자체에 추가할 경우 증가 연산자를 사용할 수 있다.
print("---------tuple 추가----------")
a += ("체리",)
# 추가되는 하나의 요소는 문자열이기 때문에 tuple 형태로 만들 때 콤마 사용
print(a)

# unpacking:구조분해 할당
print("---------unpacking----------")
(a1, b1, c1, d1, e1, f1) = a
print(a1)
print(b1)
print(c1)
print(d1)
print(e1)
print(f1)

# range: 범위
print("---------range----------")
print(range(len(a)))

# 반복문으로 요소 출력
print("---------반복문으로 요소 출력----------")
for i in range(len(a)):
    print(a[i])

# tuple 복사하여 연결
print("---------tuple 복사하여 연결----------")
print(a * 2)
