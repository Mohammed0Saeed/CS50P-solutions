from numb3rs import validate
import pytest

def test_numbers():
    assert validate("12.9.123.245") == True
    assert validate("1.1.1.1") == True
    assert validate("9.99.9.2334") == False
    assert validate("255.0.256.0") == False
    assert validate("255.0.255.0") == True

def test_punct():
    assert validate("1,1,1,1") == False

def test_letters():
    assert validate("q.q.q.q") == False
