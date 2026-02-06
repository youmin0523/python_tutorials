import random  # 데이터 섞는 모듈

a = "abcd"
a = list(a)
key = a.copy()
print(a)

random.shuffle(key)  # 리스트 요소를 무작위로 섞는다.
print(key)
print("*" * 100)

plain_text = "abcd"
cipher_text = ""

for letter in plain_text:
    index = a.index(letter)
    # plain_text 리스트로 나온 문자의 순번은 a 리스트의 순번과 같기 때문에 같은 순번을 찾아서 암호화한다.
    print(f"index: {index}")
    cipher_text += key[index]
    # 암호화된 문자를 cipher_text에 추가한다.
    print(f"cipher_text: {cipher_text}")
print("*" * 100)

print("-" * 45 + "decription" + "-" * 45)

cipher_text = input("비밀키를 입력해주세요.")
plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    # key 리스트로 나온 문자의 순번은 a 리스트의 순번과 같기 때문에 같은 순번을 찾아서 복호화한다.
    print(f"index: {index}")
    plain_text += a[index]
    # 복호화된 문자를 plain_text에 추가한다.
    print(f"plain_text: {plain_text}")
print("*" * 100)
print(f"decription: {plain_text}")
print("*" * 100)
