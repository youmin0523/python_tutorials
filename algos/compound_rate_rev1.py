principal = 0
rate = 0
time = 0


def get_compound_rate(prompt):
    while True:
        value = input(prompt)
        # if time <= 0:
        #     print("Time(기간) must be greater than 0")

        try:
            value = float(value)

        except ValueError:
            print(f"{value}은 유효한 입력값이 아닙니다.")
            continue

        if value <= 0:
            print(f"{prompt}은 0보다 커야 합니다.")
            continue
        else:
            break
    return value


principal = get_compound_rate("Enter the principal amount(원금): ")
rate = get_compound_rate("Enter the annual interest rate(연이율): ")
time = get_compound_rate("Enter the time in years(기간): ")

# [A = P * (1 + r / n)^t]
# pow() : poy(x,y) -> x의 y승
# [A = principal * (1 + rate / 100) ** time]

print("*" * 120)
print("*" * 120)
print("최종금액은 다음과 같습니다.")

total = principal * pow((1 + rate / 100), time)
print(
    f"당신이 입력한 원금은 {principal}원이고, 연이율은 {rate}%, {time}년 후에 받을 수 있는 총 금액은 {total}원 입니다."
)
print("*" * 120)
print("*" * 120)
