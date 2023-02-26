def main():
    response = input("Greeting: ")
    money = value(response)
    print(f"${money}")

def value(greeting):
    greeting = greeting.lower().strip()
    temp = greeting.find("h")

    match temp:
        case 0:
            findHello = greeting.find("hello")
            if findHello == -1:
                return 20
            elif findHello == 0:
                return 0
        case _:
            return 100


if __name__ == "__main__":
    main()




