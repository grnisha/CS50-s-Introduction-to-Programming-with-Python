from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("2/4") == 50


def test_convert_error():
    with pytest.raises(ValueError):
        convert("4/2")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
