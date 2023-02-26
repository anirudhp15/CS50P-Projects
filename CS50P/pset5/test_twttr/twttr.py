def main():
    user_input = input("Input: ")
    user_output = shorten(user_input)
    print("Output: " + user_output)


def shorten(word):
    short_word = ""
    for letter in word:
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            short_word = short_word + letter
    return short_word


if __name__ == "__main__":
    main()
