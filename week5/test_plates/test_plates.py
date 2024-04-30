from plates import is_valid

def test_isValid_true():
    assert is_valid("AA1234") == True
    assert is_valid("ABF305") == True

def test_isValid_twoChars():
    assert is_valid("A8621") == False
    assert is_valid("1AA32") == False

def test_isValid_false_size():
    assert is_valid("A") == False
    assert is_valid("AAS1234567") == False

def test_isValid_false_punct():
    assert is_valid("A_535") == False
    assert is_valid("AR33.3") == False

def test_isValid_false_order():
    assert is_valid("CS50P") == False
    assert is_valid("AAA3FF") == False

def test_inValid_false_zero():
    assert is_valid("AA0") == False
