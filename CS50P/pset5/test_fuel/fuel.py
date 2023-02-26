def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    tank_status = gauge(percentage)
    print(tank_status)


def convert(fraction):
    while True:
        try:
            num, denom = fraction.split('/')
            numerator = int(num)
            denominator = int(denom)
            if numerator/denominator <= 1:
                fuel_tank = float(numerator/denominator)
                fuel_tank = int(fuel_tank*100)
                return fuel_tank
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()







