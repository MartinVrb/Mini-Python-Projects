import random

while True:
    welcome_script = input("Welcome to the Guess a number game! Are you ready for adventure? (yes/no): ")
    if welcome_script == "yes":
        print("Let's do it!")
        break
    elif welcome_script == "no":
        print("Sorry to hear that. See you next time! (:")
        exit()
    else:
        print("Invalid input! Try again.")

while True:
    zero_times_left = True
    begin = True
    first_try_guess = True
    more_tries_guess = True
    try_function_guess = True
    tries_limit = 10
    guesses = 0
    computers_choice = random.randint(1, 100)

    while begin:
        my_choice = input("Try to guess the number: ")

        if my_choice.isdigit():
            my_choice = int(my_choice)
            guesses += 1
            tries_limit -= 1

            if my_choice == computers_choice and guesses == 1:
                print("WOW! You guessed the number on the first try!")
                while first_try_guess:
                    second_ask_to_continue = input("Do you want to play one more game? (yes/no): ")
                    if second_ask_to_continue == "yes":
                        print("Great!")
                        first_try_guess = False
                        begin = False
                    elif second_ask_to_continue == "no":
                        print("Okay. See you next time! (:")
                        exit()
                    else:
                        print("Invalid input! Try again.")

            elif my_choice == computers_choice and guesses > 1:
                print(f"Congratulations! You guessed the number after {guesses} tries.")
                while more_tries_guess:
                    third_ask_to_continue = input("Do you want to play one more game? (yes/no): ")
                    if third_ask_to_continue == "yes":
                        print("Great!")
                        more_tries_guess = False
                        begin = False
                    elif third_ask_to_continue == "no":
                        print("Okay. See you next time! (:")
                        exit()
                    else:
                        print("Invalid input! Try again.")

            elif tries_limit == 0:
                print("Sorry your attempts are over and unfortunately you didn't guess the number. ""Try a little bit harder next time! (:")
                while zero_times_left:
                    first_ask_to_continue = input("Do you want to play one more game? (yes/no): ")
                    if first_ask_to_continue == "yes":
                        print("Great!")
                        begin = False
                        break
                    elif first_ask_to_continue == "no":
                        print("Okay. See you next time! (:")
                        exit()
                    else:
                        print("Invalid input! Try again.")

            elif my_choice < computers_choice:
                print("Guess higher!")
                if tries_limit > 1:
                    print(f"You have {tries_limit} tries left.")
                elif tries_limit == 1:
                    print(f"You have {tries_limit} try left.")

            elif my_choice > computers_choice:
                print("Guess lower!")
                if tries_limit > 1:
                    print(f"You have {tries_limit} tries left.")
                elif tries_limit == 1:
                    print(f"You have {tries_limit} try left.")

        else:
            print("Invalid input! Try again.")

