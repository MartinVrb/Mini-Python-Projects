number = int(input())

for i in range(number - 1, -1, -1):
    print(" " * (number - i), end="")
    for j in range(i + 1):
        print("* ", end="")
    print()
