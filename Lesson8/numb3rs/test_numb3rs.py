from numb3rs import validate


def test_numb3rs_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("258.2.3.2") == False
    assert validate("1.2.3.4") == True
    assert validate("11.99.22.88") == True
    assert validate("199.911.288.882") == False
    assert validate("249.249.249.249") == True
    assert validate("x.x.x.x") == False
    assert validate("x") == False
    assert validate("1") == False