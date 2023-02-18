while True:
    fraction = input("Fraction: ")
    nums = fraction.split('/')
    try:
        numerator = int(nums[0])
        denominator = int(nums[1])

        fuel_tank = float(numerator/denominator)
        if fuel_tank > 1:
            pass
        elif fuel_tank <= 0.01:
            print("E")
            break
        elif fuel_tank >= 0.99:
            print("F")
            break
        else:
            fuel_tank = round(fuel_tank*100)
            fuel_tank = str(fuel_tank)
            print(fuel_tank + "%")
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass





