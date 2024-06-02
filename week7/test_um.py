import pytest
from um import count

def test_um_inWord():
    assert count("um") == 1
    assert count("yum") == 0

def test_um_spaces():
    assert count(" um ") == 1
    assert count("Um") == 1
