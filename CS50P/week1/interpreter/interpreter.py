expression = input("Expression: ")
if len(expression) == 5:
    x = int(expression[0])
    y = expression[2]
    z = int(expression[4])
elif len(expression) == 6:
    x = int(expression[0:2])
    y = expression[3]
    z = int(expression[5])

if y == '+':
    answer = float(x+z)
    print(answer)
if y == '-':
    answer = float(x-z)
    print(answer)
if y == '*':
    answer = float(x*z)
    print(answer)
if y == '/':
    answer = float(x/z)
    print(answer)