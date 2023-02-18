months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        old_date = input("Date: ").lstrip()

        if is_valid(old_date):
            new_date = convert_date(old_date)
            print(new_date)
            break
        else:
            pass

def is_valid(s):
    if '/' in s:
        if s[0].isdigit() and int(s.split('/')[0]) <= 12 and int(s.split('/')[1]) <= 31 and int(s.split('/')[2]) > 0:
            return True
        else:
            return False
    elif ',' in s:
        components = s.split(maxsplit=2)
        if s[0].isdigit() or int(components[1].rstrip(',')) >= 31:
            return False
        else:
            return True
    else:
        return False

def convert_date(s):
    new_date = ""
    if '/' in s:
        day = s.split('/')[1].zfill(2)
        month = s.split('/')[0].zfill(2)
        year = s.split('/')[2].strip()
        new_date = year + '-' + month + '-' + day
        return new_date
    elif ',' in s:
        components = s.split(maxsplit=2)
        day = components[1].rstrip(',').zfill(2)
        month = str(months.index(components[0]) + 1).zfill(2)
        year = components[2]
        new_date = year + '-' + month + '-' + day
        return new_date
    else:
        print("wtf")


main()