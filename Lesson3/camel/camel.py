def main():
    camel = input("camelCase: ")
    snake = get_snake_case(camel)
    print("snake_case:",snake)

def get_snake_case(camel):
    snake = ""
    for char in camel:
        if char.isupper():
            snake += "_"
        snake += char.lower()
    return snake

main()