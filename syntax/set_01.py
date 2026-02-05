# 자료 묶음 문법 : List, Tuple, (Set), Dictionary
# Set
# 1. 인덱스로 접근할 수 없다
# 2. 내부 요소를 수정할 수 없다
# 3. 중복된 요소가 포함될 수 없다 -> 중복 데이터가 있을 경우 오류가 나지는 않지만 중복 데이터는 표현되지 않는다.
# 4. 순서가 없어서 매번 바뀐다
# 5. 중괄호를 사용한다

print("---------set test----------")
a = {1, 2, 3, 4, 5}  # 숫자는 순서가 바뀌지 않는다
print(a)

b = {"사과", "바나나", "체리", "파인애플"}
print(b)

c = {True, 1, 2, 3}  # True 는 1, False 는 0으로 인식. True와 1은 중복되기에 하나만 표시
print(c)

# 생성자 사용
print("---------생성자 사용----------")
d = set(("a", "b", "c"))
print(d)
print(type(d))

# 존재 여부
print("---------존재 여부----------")
e = "사과" in b
print(e)

# 요소 추가:add()
print("---------요소 추가----------")
b.add("포도")  # 추가 위치는 정해지지 않는다
print(b)

# 여러 요소 추가:update()
print("---------여러 요소 추가----------")
b.update(a)
print(b)

# 요소 삭제:remove()
print("---------요소 삭제----------")
print(b)
b.remove("사과")
# b.remove("망고")  # remove는 존재하지 않는 요소를 삭제하면 Error 발생
print(b)

# 요소 삭제:discard()
print("---------요소 삭제----------")
print(b)
b.discard("포도")
b.discard("망고")  # discard는 존재하지 않는 요소를 삭제해도 Error는 발생하지 않는다
print(b)

# 요소 삭제:pop()
print("---------요소 삭제----------")
print(b)
b.pop()  # pop은 임의의 요소가 삭제됨
print(b)
