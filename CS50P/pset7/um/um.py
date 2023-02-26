import re


def main():
    print(count(input("Text: ")))


def count(s):
    ums = re.findall(r"\b(um\b)|(Um)|('...')", s)
    return len(ums)


if __name__ == "__main__":
    main()

    #\b\W*um[^m]*\W*