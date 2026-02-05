# 1. 문자열
x = "hello"

# 2. 숫자: 정수, 실수 (float), 복소수(complex)
y = 20
z = 3.5
w = 1j

print(type(y))
print(type(z))
print(type(w))
print(w)

# 3. list: 순서가 있는 데이터 집합
b = ["apple", "banana", "cherry"]
print(type(b))
print(b[1])

# 4. tuple: 순서가 있는 데이터 집합 (수정 불가)
c = ("apple", "banana", "cherry")
print(type(c))
print(c[2])

# 5. set: 순서가 없는 데이터 집합
d = {"apple", "banana", "cherry"}
print(type(d))
print(d)

# 6. dict: key, value 형태의 데이터 집합 (자바스크립트 객체와 같음)
e = {"apple": "red", "banana": "yellow", "cherry": "red"}
print(type(e))
print(e["apple"])

# 7. boolean: True, False
f = True
print(type(f))

# 8. NoneType: None
g = None
print(type(g))

# 9. 여러줄의 문자열
h = """lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(h)
