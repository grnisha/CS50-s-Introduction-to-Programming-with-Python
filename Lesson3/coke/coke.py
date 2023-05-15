AMOUNT_DUE = 'Amount Due:'
INSERT_COIN = 'Insert Coin: '
CHANGE_OWED = 'Change Owed:'
PRICE = 50

def main():
    amount_due = PRICE
    while(amount_due > 0):
        inserted = prompt_user(amount_due)
        amount_due = calculate(amount_due, inserted)

    print(CHANGE_OWED, abs(amount_due))



#Print amount due and prompt user to insert balance and validate input
def prompt_user(amount):
    inserted = 0
    while(inserted not in [5, 10, 25]):
        print(AMOUNT_DUE, amount)
        inserted = int(input(INSERT_COIN))
    return inserted

#Calculate balance based on inserted amount
def calculate(amount_due,inserted):
    return amount_due - inserted


if __name__ == '__main__':
    main()
