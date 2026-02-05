a = {"사과", "바나나"}
b = {"사과", "체리"}

# union: 두개의 set을 새로운 변수에 합쳐서 담는다
print("---------union----------")
c = a.union(b)  # 중복이 제거된다
print(c)

# clear: set을 비운다
print("---------clear----------")
# a.clear()
print(a)  # 객체 공간은 유지하고 요소만 삭제한다

# copy: 복사
print("---------copy----------")
d = b.copy()
print(d)

# difference:차집합
print("---------difference----------")
print(a)
e = a.difference(b)
print(e)

# intersection:교집합
print("---------intersection----------")
print(a)
f = a.intersection(b)
print(f)

# symmetric_difference:a와 b의 합집합에서 교집합 제거 -> 대칭차집합
print("---------symmetric_difference----------")
print(a)
g = a.symmetric_difference(b)
print(g)
