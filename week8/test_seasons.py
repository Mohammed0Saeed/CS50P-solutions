import pytest
from seasons import minutes_in_words

def test_minutsInWords():
    assert minutes_in_words("2023-06-26") == "Five hundred twenty-five thousand, six hundred minutes"
    assert minutes_in_words("2022-06-26") == "One million, fifty-one thousand, two hundred minutes"