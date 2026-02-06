# compound interest calculator : Compound interest calculator는 원금(principal)과 이자가 누적되어 이자에 이자가 붙는 방식으로 계산되는 복리(Compound Interest)를 계산하는 도구입니다. 복리 계산은 다음과 같은 수식을 사용합니다:

# [ A = P * (1 + r / n)^t ]

# ( A )는 최종 금액 (원금 + 이자)
# ( P )는 초기 원금 (Principal)
# ( r )는 연이율 (Annual interest rate, 소수로 표현)
# ( n )는 연간 복리 계산 횟수 (Compounding frequency per year)
# ( t )는 시간 (연 단위, Time in years)

# Flow
# 1. 사용자로부터 필요한 값들을 입력받습니다.
#    - 초기 원금 (P)
#    - 연이율 (r)
#    - 복리 계산 횟수 (n)
#    - 기간 (t)

# 2. 입력받은 값들을 사용하여 복리 계산 공식을 적용합니다.

# 3. 계산된 최종 금액을 사용자에게 보여줍니다.


principal = 0
rate = 0
time = 0

while True:  # while문은 조건이 참인 동안 반복한다.
    principal = input("Enter the principal amount(원금): ")

    # if principal <= 0:  # if문은 조건이 참일 때만 실행한다.
    #     print("Principal(원금) amount must be greater than 0")

    try:
        principal = float(principal)

    except ValueError:
        print(f"{principal}은 유효한 입력값이 아닙니다.")
        continue

    if principal <= 0:
        print("Principal(원금) amount must be greater than 0")
        continue
    else:
        break

while True:
    rate = input("Enter the annual interest rate(연이율): ")
    # if rate <= 0:
    #     print("Interest rate(이자율) must be greater than 0")

    try:
        rate = float(rate)

    except ValueError:
        print(f"{rate}은 유효한 입력값이 아닙니다.")
        continue

    if rate <= 0:
        print("Interest rate(이자율) must be greater than 0")
        continue
    else:
        break


while True:
    time = input("Enter the time in years(기간): ")
    # if time <= 0:
    #     print("Time(기간) must be greater than 0")

    try:
        time = float(time)

    except ValueError:
        print(f"{time}은 유효한 입력값이 아닙니다.")
        continue

    if time <= 0:
        print("Time(기간) must be greater than 0")
        continue
    else:
        break

# print(f"Principal(원금): {principal}")
# print(f"Interest rate(연이율): {rate}")
# print(f"Time(기간): {time}")
# print(f"{principal * (1 + rate / 100) ** time} 원 입니다.")

# [A = P * (1 + r / n)^t]
# pow() : poy(x,y) -> x의 y승
# [A = principal * (1 + rate / 100) ** time]

print("*" * 100)
print("*" * 100)
print("최종금액은 다음과 같습니다.")

total = principal * pow((1 + rate / 100), time)
print(
    f"당신이 입력한 원금은 {principal}원이고, 연이율은 {rate}%, {time}년 후에 받을 수 있는 총 금액은 {total}원 입니다."
)
print("*" * 100)
print("*" * 100)
