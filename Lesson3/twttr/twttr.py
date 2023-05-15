def main():
    user_input = input("Input: ")
    print("output:", format_text(user_input))

#function to remove vowels from a string case insetive
def format_text(user_input):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = ""
    for char in user_input:
        if char.lower() not in vowels:
            output += char
    return output

'''
def format_text(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for vowel in vowels:
        text = text.replace(vowel, '')
    return text
'''

if __name__ == '__main__':
    main()