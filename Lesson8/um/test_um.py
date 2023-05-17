from um import count

def test_count():
    text1 = "hello, um, world"
    assert count(text1) == 1

    text2 = "yummy"
    assert count(text2) == 0

    text3 = "Um, um, UM, um"
    assert count(text3) == 4

    text4 = "The quick brown fox jumps over the lazy dog"
    assert count(text4) == 0

    text5 = "um-um-um"
    assert count(text5) == 3

    text6 = "The um is a word, but the word umbrella is not um"
    assert count(text6) == 2