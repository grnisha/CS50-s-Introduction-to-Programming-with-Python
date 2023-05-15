from bank import value


def test_value_hello():
    assert value("hello") == "$0"
    assert value("Hello") == "$0"
    assert value("HELLO") == "$0"
    assert value("hElLo") == "$0"
    assert value(" hello ") == "$0"


def test_value_h():
    assert value("h") == "$20"
    assert value("H") == "$20"
    assert value("    H") == "$20"
    assert value("h   ") == "$20"


def test_value_others():
    assert value("python") == "$100"
    assert value("ABCD") == "$100"
    assert value("xyz") == "$100"
    assert value("123!") == "$100"
    assert value("") == "$100"
