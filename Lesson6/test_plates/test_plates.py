from plates import is_valid


# “All vanity plates must start with at least two letters.”
def test_plates_begin_with_two_letters():
    assert is_valid("ABP10") == True
    assert is_valid("10") == False
    assert is_valid("A10") == False
    assert is_valid("A") == False


# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def test_length():
    assert is_valid("ABP10") == True
    assert is_valid("AB") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEF10") == False


# “Numbers cannot be used in the middle of a plate; they must come at the end.
#  For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
def test_num():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False


# “No periods, spaces, or punctuation marks are allowed.”
def test_punct():
    assert is_valid("AB10:") == False