# isalpha() : 알파벳 문자열인지 확인
a = "ABC"
b = "A2C"
c = "A B"
print(a.isalpha())
print(b.isalpha())
print(c.isalpha())


# isnumeric() : 숫자 문자열인지 확인
d = "123"
e = 123  # 오류 발생
print(d.isnumeric())
# print(e.isnumeric())

print("---------------")


# isalnum (): 알파벳 또는 숫자인지 확인
f = "abc"
g = "123"
h = "123abc"
i = "123 abc"
print(f.isalnum())
print(g.isalnum())
print(h.isalnum())
print(i.isalnum())

print("---------------")


# isspace() : 공백 문자열인지 확인
j = ""
k = "aaa"
print(j.isspace())
print(k.isspace())

print("---------------")

# join(): 문자열 연결
my_list = ["aa-bb-cc", "dd-ee-ff", "gg-hh-ii"]
my_list_tuple = ("aa-bb-cc", "dd-ee-ff", "gg-hh-ii")
rs = ", ".join(my_list)
rst = ",".join(my_list_tuple)
print(rs)
print(rst)

print("---------------")

# splitlines() : 여러 줄로 이뤄진 문자열을 분리하여 리스트로 변환
s = "Hello \nMy name is marshall"

print(s.splitlines())

print("---------------")

# find(): 문자열에서 특정 문자열을 찾아 인덱스를 반환
t = "Hello man My name is Marshall"
print(t.find("man"))
print(t.find("more"))  # 없을 경우 -1 반환
