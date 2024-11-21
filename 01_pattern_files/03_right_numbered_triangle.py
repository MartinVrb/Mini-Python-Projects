largest_count = int(input())
my_num = 0
final = ""

for row in range(1, largest_count + 1):
    while my_num < row:
        my_num += 1
        final += str(my_num)

    print(final)
    final = ""
    my_num = 0