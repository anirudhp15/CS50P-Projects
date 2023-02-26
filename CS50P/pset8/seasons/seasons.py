from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():
    birthday = input("What is your date of birth? ")
    try:
        year, month, day = check_birthday(birthday)
    except:
        sys.exit("Invalid Date")

    date_of_birth = date(int(year), int(month), int(day))
    date_of_today = date.today()
    time_delta = date_of_today - date_of_birth
    minutes = time_delta.days * 24 * 60
    words = p.number_to_words(minutes, andword="")
    print(words.capitalize() + " minutes")


def check_birthday(birthday):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birthday):
        year, month, day = birthday.split("-")
        return year, month, day

if __name__ == "__main__":
    main()