from bank import value

def test_return_zero():
    assert value("hello") == 0
    assert value("Hello, Newman") == 0
    assert value("Hello WORLD") == 0

def test_return_twenty():
    assert value("hi") == 20
    assert value("Hey there") == 20
    assert value("HOWDY") == 20

def test_return_hundred():
    assert value("What's up?") == 100
    assert value("Good Morning") == 100
    assert value("123 greeting") == 100
    
