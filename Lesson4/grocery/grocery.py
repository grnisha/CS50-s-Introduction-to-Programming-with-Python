list ={}

def main():
    while True:
        try:
            add_to_list(input().upper())
        except EOFError:
            break

    print_grocery()

def print_grocery():
    #sort dictionary in alphabetical order of keys
    sorted_list = sorted(list)

    #print sorted dictionary
    for item in sorted_list:
        print(f'{list[item]} {item}')


def add_to_list(item):
    if item in list:
        list[item] += 1
    else:
        list[item] = 1

if __name__ == '__main__':
    main()
