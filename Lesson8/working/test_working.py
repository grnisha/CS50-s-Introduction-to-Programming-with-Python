import pytest
from working import convert


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("5 PM to 8 AM") == "17:00 to 08:00"
    assert convert("5:30 PM to 7:10 AM") == "17:30 to 07:10"


def test_value_error():
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("28:00 AM to 9:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
