largest_count = int(input())
counter = 0

for times in range(1, largest_count + 1):
    final = "* " * times
    print(final)
    counter += 1
    if counter == largest_count:
        for second_times in range(largest_count - 1, 0, -1):
            second_final = "* " * second_times
            print(second_final)
