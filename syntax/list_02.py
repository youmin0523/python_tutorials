a = ["사과", "바나나", "체리", "오렌지", "키위", "망고", "사과"]

for x in a:
    print(x)

print("---------sort----------")

# sort(): 정렬
a.sort()  # 별도 변수에 저장할 수 없다
print(a)

print("---------sort(reverse=True)----------")

# sort(reverse=True) : 역순 정렬
a.sort(reverse=True)
print(a)

print("---------copy()----------")

# 리스트 복사시 b = a 형식으로 복사하면 같은 주소를 참조하기 때문에 a,b 모두 바뀌게 된다. 따라서 복사할 때는 copy()를 사용한다.
b = a.copy()
a[0] = "포도"

print(a)
print(b)

print("---------list()----------")

# list(): 특정 리스트를 담아서 새로운 리스트를 반환
c = list(a)
print(c)
c[0] = "수박"
print(a)
print(c)

print("---------리스트 합치기----------")

# 리스트 합치기
d = ["new list 1", "new list 2"]
e = a + d
print(e)

print("---------for문 이용----------")

# for문 이용

for x in d:
    a.append(x)
print(a)

print("---------extend()----------")

# extend(): 리스트에 다른 리스트를 추가
a.extend(d)
print(a)
