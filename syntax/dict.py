# 자료 묶음 문법 : List, Tuple, Set, (Dictionary)
# Dictionary
# 1. 중복이 허용되지 않는다
# 2. 변경이 가능하다
# 3. 순서가 없다
# 4. Key Value 쌍으로 구성된다
# 5. 자바스크립트의 객체와 유사하다

print("---------Dict test----------")
a = {
    "name": "marshall",
    "age": "20",
    "address": "seoul",
    "gu": ["Gangnam", "dobong", "guro"],
}

print(a)
print(type(a))

# 데이터 접근
print("---------데이터 접근----------")
print(a["name"])
print(a["gu"][0])

# get으로 접근
print("---------get으로 접근----------")
print(a.get("name"))

# key값만 출력
print("---------key값만 출력----------")
print(a.keys())

# value값만 출력
print("---------value값만 출력----------")
print(a.values())

# 길이
print("---------길이----------")
print(len(a))  # 4개의 키가 있다

# 생성자 사용
print("---------생성자 사용----------")
b = dict(name="marshall", age="20")
print(b)

# 요소의 변경
print("---------요소의 변경----------")
a["age"] = 30
a.update({"name": "key"})
print(a)

# 요소의 추가
print("---------요소의 추가----------")
a["color"] = ["red", "green", "blue"]
print(a)

#
for x in a:
    print(x.get("name"))
