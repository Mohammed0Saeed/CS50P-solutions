import pytest
from response import isValid

def test_correct_email():
    assert isValid("s.mohddheia@gmail.com") == "Valid"
    assert isValid("info@cs50.harvard.edu") == "Valid"
    assert isValid("modo_4u@web.de") == "Valid"

def test_incorrect_email():
    assert isValid("s.mohddheia@gmail") == "Invalid"
    assert isValid("info.de") == "Invalid"
    assert isValid("@gmail.com") == "Invalid"
    assert isValid("cat!") == "Invalid"
