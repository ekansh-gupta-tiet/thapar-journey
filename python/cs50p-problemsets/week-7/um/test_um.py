from um import count


def test_standalone_um():
    assert count("um") == 1
    assert count("hello, um, world") == 1
    assert count("um, thanks, um, for the help") == 2


def test_case_insensitivity():
    assert count("UM") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("UM, UM, um!") == 3


def test_substring_ignore():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("instrumentation") == 0
    assert count("circumference") == 0
