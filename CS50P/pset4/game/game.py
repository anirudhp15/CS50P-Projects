import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
        else:
            pass

    except ValueError:
        pass


random_int = random.randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < random_int:
                print("Too Small!")
            elif guess > random_int:
                print("Too Large!")
            else:
                print("Just Right!")
                break
    except:
        pass
