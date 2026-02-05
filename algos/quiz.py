# Tuple을 사용한 퀴즈

questions = (
    "주기율표의 원소는 몇개 인가요?: ",
    "가장 큰 알을 낳는 동물은?: ",
    "지구상에서 가장 흔한 물질은 무엇인가요?: ",
    "사람의 뼈는 몇개 인가요?: ",
    "태양계에서 가장 큰 행성 이름은 무엇인가요? ",
)
options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. 고래", "B. 악어", "C. 코끼리", "D. 타조"),
    ("A. 질소", "B. 산소", "C. 탄소", "D. 수소"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. 수성", "B. 금성", "C. 토성", "D. 목성"),
)
answers = ("C", "D", "A", "A", "D")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-" * 100)
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("정답을 입력해주세요 (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("정답입니다 !")
    else:
        print("오답입니다 !")
        print(f"정답은 {answers[question_num]}입니다.")

    question_num += 1

print("-" * 100)
print("-" * 47, "결과", "-" * 47)
print("-" * 100)

score = int(score / len(questions) * 100)
print(f"당신의 점수는 {score}점 입니다.")
