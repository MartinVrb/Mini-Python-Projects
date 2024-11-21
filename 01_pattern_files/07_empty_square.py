rows = int(input())
columns = int(input())

for i in range(rows):
    for j in range(columns):
        if i in (0, rows - 1) or (0 <= i < rows and j in (0, columns - 1)):
            print("* ", end="")
        else:
            print(" ", end=" ")
    print()
