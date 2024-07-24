from jar import Jar
import pytest


def test_init():
    jar = Jar(12, 5)
    assert jar.__str__() == "🍪🍪🍪🍪🍪"

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    assert jar.deposit(4) == 4
    assert jar.deposit(3) == 7

def test_withdraw():
    jar = Jar(12, 6)
    assert jar.withdraw(2) == 4
    assert jar.withdraw(1) == 3
