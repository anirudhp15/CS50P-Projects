from seasons import check_birthday

def main():
    test_check_birthday()


def test_check_birthday():
    assert check_birthday("2004-10-15") == ("2004", "10", "15")
    assert check_birthday("2004-1-5") == None
    assert check_birthday("October 15, 2004") == None


if __name__ == "__main__":
    main()