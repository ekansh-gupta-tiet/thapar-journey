from plates import is_valid

def test_valid_plates():
    assert is_valid("CS50") is True
    assert is_valid("ECT088") is True
    assert is_valid("NRV0US") is True

def test_beginning_letters():
    assert is_valid("A") is False
    assert is_valid("50CS") is False
    assert is_valid("C5") is False

def test_length_constraints():
    assert is_valid("H") is False
    assert is_valid("OUTATIME") is False

def test_number_placement():
    assert is_valid("CS50P") is False
    assert is_valid("CS05") is False

def test_punctuation():
    assert is_valid("CS50P!") is False
    assert is_valid("PI3.4") is False
    assert is_valid("CS 50") is False
