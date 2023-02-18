import inflect

p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
        pass
    except EOFError:
        print()
        mylist = p.join(names)
        print("Adieu, adieu, to " + mylist)
        break
