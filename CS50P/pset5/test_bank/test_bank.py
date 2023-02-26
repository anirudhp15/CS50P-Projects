from bank import value

def main():
    test_greetings()
    test_numbers()
    test_punctuation()

def test_greetings():
    assert value('Hello') == 0
    assert value('Hey') == 20
    assert value('Welcome') == 100

def test_numbers():
    assert value('100') == 100


def test_punctuation():
    assert value('!?,.') == 100