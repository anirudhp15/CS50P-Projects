from numb3rs import validate
import pytest

/workspaces/125221480/pset1def main():
    test_large_num()
    test_words()


def test_large_num():
    assert validate("255.255.255.255") == True
    assert validate("500.255.255.255") == False
    assert validate("18.255.260.255") == False
    assert validate("1.1.1.1") == True
    assert validate("123.0.0.17") == True


def test_words():
    assert validate("cat") == False

if __name__ == "__main__":
    main()