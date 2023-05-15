import inflect

enj = inflect.engine()
names =[]
def main():
    while True:
        try:
            names.append(input("Name:"))
        except EOFError:
            break
    print(enj.join(names, final_sep=""))

if __name__ == "__main__":
    main()


