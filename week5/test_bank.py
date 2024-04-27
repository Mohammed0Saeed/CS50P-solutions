from bank import value

def test_greeting():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("how are you?") == 20
    assert value("How u doin?") == 20
    assert value("wussap?") == 100
