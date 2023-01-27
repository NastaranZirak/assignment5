def checkered ():
    column = int(input("Enter the first number"))
    row = int(input("Enter the second number"))
    matrix = []
    for x in range(column):
        a = []
        b = []
        for y in range(row):
            a.append("o")
            a.append("@")
            b.append("o")
            b.append("@")

            matrix.append(a)
            matrix.append(b)

    for x in range(column):
        for y in range(row):

            print(matrix[x][y], end = "")

        print()

checkered()
