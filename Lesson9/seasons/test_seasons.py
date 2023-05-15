from seasons import get_minutes, get_text
from datetime import date


def test_get_text():
    assert get_text(525600) == "Five hundred twenty-five thousand, six hundred"
    assert get_text(1051200) == "One million, fifty-one thousand, two hundred"

def test_get_minutes():
    assert get_minutes("2022-04-25", date(2023, 4, 25)) == 525600

