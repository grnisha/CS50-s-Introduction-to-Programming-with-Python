def main():
    word = input("Input: ")
    print("output:", shorten(word))

#function to remove vowels from a string case insetive
def shorten(word):
    vowels = ['a', 'e', 'i', 'o']
    output = ""
    for char in word:
        if char.lower() not in vowels:
            output += char
    return output

'''
def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for vowel in vowels:
        word = word.replace(vowel, '')
    return word
'''

if __name__ == '__main__':
    main()