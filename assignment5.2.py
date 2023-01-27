import math

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
if a >= 0:
    answer = -(c / b)
    print("x = ", answer)
else:
    r = float(math.sqrt((b * b) - (a * c * 4)))
    x1 = int((-b + r) / (a * 2))
    x2 = float((-b - r) / (a * 2))

    answer1 = x1
    answer2 = x2

    print("x1 = ", answer1)
    print("x2 = ", answer2)