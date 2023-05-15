
'''
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
'''

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return check_length(s) and check_first_two(s) and check_char_set(s) and check_numbers(s)

        
#Validate length
def check_length(s):
    if len(s) < 2 or len(s) > 6:
        return False
    return True

#Validate first two characters
def check_first_two(s):
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    return True

#Validate Character Set is alpahnumeric
def check_char_set(s):
    for c in s:
        if not c.isalnum():
            return False
    return True


#Find first number in the string
def find_first_digit_index(s):
    for i, c in enumerate(s):
        if c.isdigit():
            return i
        
#Validate no numbers in the middle and the first number is not zero
def check_numbers(s):
    first_digit = find_first_digit_index(s)
    if first_digit is not None and (s[first_digit] == '0' or not(s[first_digit:].isdigit())):
        return False
    return True


main()
