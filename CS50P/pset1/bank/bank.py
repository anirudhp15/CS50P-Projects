response = input("Greeting: ").lower().strip()
greeting = response.find("h")

match greeting:
    case 0:
        findHello = response.find("hello")
        if findHello == -1:
            print("$20")
        elif findHello == 0:
            print("$0")
    case _:
        print("$100")
