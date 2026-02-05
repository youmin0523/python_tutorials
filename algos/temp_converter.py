unit = input("변환할 온도 체계를 정해주세요 (C or F): ")

if unit != "C" and unit != "F":
    print(f"{unit}은 변환할 수 없는 온도체계입니다.")
    exit()

temp = float(input("온도를 입력해주세요: "))

C_or_F = ""

try:
    temp = float(temp)
except ValueError:
    print(f"{temp}는 유효하지 않은 문자열입니다. 숫자로 입력해주세요.")
    exit()

if unit.lower() == "C":
    temp = round((temp * 9 / 5) + 32)
    C_or_F = "화씨"
elif unit.lower() == "F":
    temp = round((temp - 32) * 5 / 9)
    C_or_F = "섭씨"

print(f"변환한 온도는 {C_or_F} {temp}도 입니다.")
