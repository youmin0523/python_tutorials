print("---------Dict test----------")
a = {
    "name": "marshall",
    "age": 20,
    "address": "seoul",
    "hobby": ["reading", "traveling", "sports"],
}

# key값만 출력
print("---------key값만 출력----------")
for x in a.keys():
    print(x)

# value값만 출력
print("---------value값만 출력----------")
for x in a.values():
    print(x)

# items
print("---------items----------")
print(a.items())  # key-value를 Tuple 리스트로 출력

# key-value 쌍으로 출력
print("---------key-value 쌍으로 출력----------")
for key, value in a.items():
    print(key, value)
