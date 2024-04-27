from twttr import shorten
import pytest

def test_lowerWord():
    assert shorten("twitter") == "twttr"

def test_upperWord():
    assert shorten("TWITTER") == "TWTTR"

def test_numbers():
    assert shorten("9") == "9"

def test_punct():
    assert shorten("h,ello") == "h,ll"

def test_empty():
   assert shorten("") == ""
