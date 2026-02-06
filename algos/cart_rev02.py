foods = []
prices = []
total = 0

while True:
    food = input("음식을 입력해주세요. 종료는 q를 입력해주세요.")
    if food == "q":
        break
    else:
        foods.append(food)
        price = int(input(f"{food}의 가격을 입력해주세요."))

        prices.append(price)
        total += price

print("---Your Cart---")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"총 카트에 담긴 상품의 가격 총액은 {total}원 입니다.")
