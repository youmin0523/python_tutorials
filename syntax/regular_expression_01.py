# 정규표현식이란 문자열을 처리하는 방법 중의 하나로 특정한 조건의 문자를 '검색'하거나 '치환'하는 과정을 매우 간편하게 처리할 수 있도록 하는 수단이다.

import re

# search
print("---------search----------")

a = "I live in Korea, Incheon 13"
# ^: 문자열의 시작
# $: 문자열의 끝
# . : 임의의 문자
# *: 전체

# I로 시작해서 Incheon으로 끝나는 문자열 검색
b = re.search("^I.*Incheon$", a)
print(b)

# findall(): 매칭되는 모든 문자열을 리스트로 반환
print("---------findall----------")
c = re.findall("[a-zA-Z0-9]", a)
# //! [Original Code] SyntaxWarning: '\d', '\D'는 유효한 이스케이프 시퀀스가 아니므로 경고 발생
# d = re.findall("\d", a)  # digit(숫자)만 검색
# e = re.findall("\D", a)  # non-digit(숫자가 아닌) 문자만 검색

# //* [Modified Code] r"" (raw string)을 사용하여 백슬래시를 문자로 취급하도록 수정
d = re.findall(r"\d", a)  # digit(숫자)만 검색
e = re.findall(r"\D", a)  # non-digit(숫자가 아닌) 문자만 검색
print(c)
print(d)
print(e)

f = re.findall("K.*a", a)  # K로 시작해서 a로 끝나는 문자열
print(f)
g = re.findall("Kore.+a", a)
# Kore와 a 사이에 어떤 문자가 1개 이상 있는 문자열 추출 Korema, koremoa... 등으로 수정하면 찾을 수 있음
print(g)
h = re.findall("live|Korea", a)
print(h)
