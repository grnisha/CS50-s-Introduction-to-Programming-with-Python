import re


def main():
    print(count(input("Text: ")))


def count(s):
    #\b: Word boundary anchor. It matches the position where a word character is not followed or preceded by another word character.
    # In this case, it ensures that "um" is not part of a larger word.
    pattern = r"\bum\b"
    return len(re.findall(pattern, s, re.IGNORECASE))


if __name__ == "__main__":
    main()
