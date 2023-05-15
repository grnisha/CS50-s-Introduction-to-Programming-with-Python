def main():
    percentage = calculate_fuel()
    if percentage <= 1:
        print('E')
    elif percentage >= 99:
        print('F')
    else:
        print(f'{percentage:.0f}%')

def calculate_fuel():
    while True:
        try:
            x,y=map(int,input('Fraction: ').split('/'))
            if(x>y):
                raise ValueError
            return round(x/y*100,0)
        except (ValueError,ZeroDivisionError):
            pass
    

if __name__ == '__main__':
    main()