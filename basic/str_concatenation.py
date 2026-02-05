# 문자열 연결
a = "Hello"
b = " World"

print(a + b)

# 문자열 포맷팅
name = "Alice"
age = 20
txt1 = "My Name is {}, I am {} years old.".format(name, age)
txt2 = "My Name is {1}, I am {0} years old.".format(age, name)
print(txt1)
print(txt2)


# f-string
print(f"My Name is {name}, I am {age} years old.")

# escape : https://zzozzomin08.tistory.com/39
# 1. 내부 특수문자
hello = "hello. my age is '20' years old."
print(hello)
print('hello. my age is "20" years old.')
print('hello. my age is "20" years old.')  # \\\" \\\" 으로 사용 가능

# 2. 문자열 개행 \n을 통해 줄 나눠짐
hello = "hello \nmy age is 20 years old."
print(hello)

# 3. 문자열 탭 \t을 통해 탭 나눠짐 (탭 만큼 띄어짐)
hello = "hello\tmy age is 20 years old."
print(hello)

# 4. 백스페이스 \b을 통해 백스페이스 나눠짐
hello = "hello\bmy age is 20 years old."
print(hello)
