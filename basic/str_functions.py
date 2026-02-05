# center: 문자열을 중앙에 위치시키는 기능
a = "world!"
b = a.center(10)
c = a.center(20)
dummy = "12345678901234567890"

print(a)
print(b)
print(c)
print(dummy)


# count: 문자열에서 특정 문자열 갯수 확인
d = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Autem commodi mollitia, quidem dolor atque, odit est pariatur velit magni, repellat ullam nisi sit eligendi accusantium quas, repellendus beatae, voluptas hic.error!"
print(d.count("a"))


# endswith: 문자열이 특정 문자열로 끝나는지 확인
e = d.endswith("error!")
f = d.endswith("error")
print(e)
print(f)


# split: 특정 문자열 기준으로 분리
g = d.split(",")
print(g)
print(type(g))
