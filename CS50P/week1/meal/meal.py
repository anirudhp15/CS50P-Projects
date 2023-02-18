from math import trunc

def main():
    mealTime = input("What time is it? ")
    hours = convert(mealTime)
    if hours >= 7 and hours <= 8:
        print("breakfast time")
    if hours >= 12 and hours <= 13:
        print("lunch time")
    if hours >= 18 and hours <= 19:
        print("dinner time")

def convert(time):
    dec = float(time.replace(":", "."))
    hours = trunc(dec)
    temp = float(dec - hours)
    mins = float(temp/0.6)
    return hours + mins

main()