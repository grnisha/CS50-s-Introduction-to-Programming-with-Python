def main():
    x, y, z = input('Expression: ').split(" ")
    print("%.1f" % calculate(x, y, z))

def calculate(x, y, z):
    if y == '+':
        return float(x) + float(z)
    elif y == '-':
        return float(x) - float(z)
    elif y == '*':
        return float(x) * float(z)
    else:
        return float(x) / float(z)

main()