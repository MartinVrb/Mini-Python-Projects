n = int(input())
# Top half of the diamond
for i in range(1, n + 1):
    # Print spaces
    print(" " * (n - i), end="")

    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end="")

    # Print decreasing numbers
    for k in range(i - 1, 0, -1):
        print(k, end="")

    print()  # Newline after each row

# Bottom half of the diamond
for i in range(n - 1, 0, -1):
    # Print spaces
    print(" " * (n - i), end="")

    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end="")

    # Print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()  # Newline after each row
