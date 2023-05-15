from twttr import shorten

def test_shorten_All():
    assert shorten("Hello World Aeiou123!") == "Hll Wrld 123!"

def test_shorten_A():
    assert shorten("AL") == "L"