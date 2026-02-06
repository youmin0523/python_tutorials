# 프로그램이 시작되면 음식 이름 입력을 받는다
# 받은 음식은 foods 리스트에 추가된다.
# q를 입력하면 종료된다
# 음식의 가격을 묻는다.
# 받은 가격은 prices 리스트에 추가된다.
# 종료되면 선택한 모든 음식을 출력한다.
# 선택한 모든 음식의 가격을 합산하여 출력한다.

foods = []
prices = []
total = 0

# CASE 1. while True
while True:
    food = input("음식을 입력해주세요: ")
    if food == "q":
        break
    price = int(input("가격을 입력해주세요: "))
    foods.append(food)
    prices.append(price)
    total += price

print("*" * 24 + "CART" + "*" * 24)
print("음식\t\t가격")
print("*" * 50)
for i in range(len(foods)):
    print(foods[i], "\t\t", prices[i], "원")
print("총 금액\t\t", f"{total}원")
print("*" * 22 + "감사합니다" + "*" * 22)
