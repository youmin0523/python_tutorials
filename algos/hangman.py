from hangman_words import words
import random

hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\"),
}
# print(hangman_art[0])

# for line in hangman_art[6]:
#     print(line)


def display_man():
    pass


def display_hint(hint):
    print(" ".join(hint))


def display_answer():
    pass


def main():
    answer = random.choice(words)  # words 튜플에서 랜덤한 하나의 단어를 선택
    # print(answer)
    hint = ["_"] * len(answer)
    # print(hint)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_hint(hint)
        print(f"\n단어: {' '.join(hint)}")
        print(f"오답 횟수: {wrong_guesses}")
        print(f"추측한 문자: {', '.join(sorted(guessed_letters))}")

        for line in hangman_art[wrong_guesses]:
            print(line)

        guess = input("알파벳을 입력해주세요: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("영문 알파벳 한 글자만 입력해주세요.")
            continue

        if guess in guessed_letters:
            print(f"{guess}는 이미 입력한 알파벳입니다.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            print("정답입니다!")
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess
        else:
            print("오답입니다.")
            wrong_guesses += 1

        if "_" not in hint:
            print(f"\n축하합니다! 정답은 '{answer}'입니다.")
            is_running = False

        if wrong_guesses >= 6:
            print(f"\n게임 오버! 정답은 '{answer}'입니다.")
            is_running = False


if __name__ == "__main__":
    main()
