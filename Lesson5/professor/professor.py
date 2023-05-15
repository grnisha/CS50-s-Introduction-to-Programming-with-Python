import random


def main():
    level = get_level()
    score = 0
    for _ in range(0, 10):
        first = generate_integer(level)
        second = generate_integer(level)
        ans = first + second
        for i in range(0, 3):
            try:
                user_ans = int(input(f"{str(first)} + {str(second)} = "))
                if user_ans == ans:
                    score += 1
                    break
            except ValueError:
                pass

            if i + 1 == 3:
                print(f"{str(first)} + {str(second)} = {ans}")
            else:
                print("EEE")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                continue
            return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
