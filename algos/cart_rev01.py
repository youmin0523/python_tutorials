foods = []
prices = []
total = 0
food = ""

# CASE 2. while food != "q"
while food != "q":
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
