from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("0/4") == 0
    assert convert("4/4") == 100
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("5/4")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
