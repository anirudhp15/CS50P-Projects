def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if requirement_one(s) == True and requirement_two(s) == True and requirement_three(s) == True and requirement_four(s) == True:
        return True
    else:
        return False


def requirement_one(s):
    for i in s[0:2]:
        if i.isdigit():
            return False

    return True


def requirement_two(s):
    if len(s) > 6 or len(s) < 2:
        return False
    else:
        return True


def requirement_three(s):

    nums = ""
    temp = ""
    for i in s:
        if i.isdigit():
            nums = nums + i
    for i in s:
        if i.isdigit():
            x = s.index(i)
            temp = s[x:]
            break

    if len(nums) > 0 and s[-1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return False
    elif len(nums) > 0 and nums[0] == '0':
        return False
    elif nums != temp:
        return False
    else:
        return True


def requirement_four(s):
    if s.isalnum():
        return True
    else:
        return False

if __name__ == "__main__":
    main()