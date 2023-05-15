def main():
    greeting = input("Greeting: ").lower().strip()
    print(get_reward(greeting))

def get_reward(greeting):
    if greeting.startswith('hello'):
        return '$0'
    elif greeting.startswith('h'):
        return '$20'
    else :
        return '$100'
    
main()
