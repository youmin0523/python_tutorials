import random

# print("\u25cf \u250c \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

dice_art = {
    1: ("┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("┌─────────┐", "│ ●       │", "│         │", "│       ● │", "└─────────┘"),
    3: ("┌─────────┐", "│ ●       │", "│    ●    │", "│       ● │", "└─────────┘"),
    4: ("┌─────────┐", "│ ●     ● │", "│         │", "│ ●     ● │", "└─────────┘"),
    5: ("┌─────────┐", "│ ●     ● │", "│    ●    │", "│ ●     ● │", "└─────────┘"),
    6: ("┌─────────┐", "│ ●     ● │", "│ ●     ● │", "│ ●     ● │", "└─────────┘"),
}


def roll_dice():
    return random.randint(1, 6)


def display_dice(result):
    for line in dice_art[result]:
        print(line)


def main():
    while True:
        input("주사위를 던지려면 Enter를 누르세요...")
        result = roll_dice()
        display_dice(result)

        again = input("다시 던지시겠습니까? (y/n): ").lower()
        if again != "y":
            print("게임을 종료합니다.")
            break


if __name__ == "__main__":
    main()
