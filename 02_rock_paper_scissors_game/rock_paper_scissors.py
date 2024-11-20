import random

is_it_invalid = True
my_result = 0
computers_result = 0

print("Welcome!")
while True:
    beginning = input("Do you want to play rock-paper-scissors? (Yes/No): ")
    if beginning == "Yes":
        print("Let's go!")
        break
    elif beginning == "No":
        print("See you next time!")
        exit()
    else:
        print("Invalid input. Try again.")

while True:
    choice = input("Choose between: Rock, Paper or Scissors: ")
    if choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid input. Try again.")
        is_it_invalid = False
    else:
        is_it_invalid = True

    if is_it_invalid:
        computers_choice_number = random.randint(1, 3)
        computers_choice = ""

        if computers_choice_number == 1:
            computers_choice = "Rock"
        elif computers_choice_number == 2:
            computers_choice = "Paper"
        elif computers_choice_number == 3:
            computers_choice = "Scissors"

        if choice == "Rock" and computers_choice == "Scissors" \
                or choice == "Scissors" and computers_choice == "Paper" \
                or choice == "Paper" and computers_choice == "Rock":
            my_result += 1
            print(f"I choose {computers_choice}.")
            print(f"Congratulations, you win! {choice} beats {computers_choice}.")
            print(f"Point for you! The result is: {my_result}:{computers_result}")
            while True:
                first_ask_to_continue = input("Do you want to continue? (Yes/No): ")
                if first_ask_to_continue == "Yes":
                    print("Very well!")
                    break
                elif first_ask_to_continue == "No":
                    print(f"The final result is: {my_result}:{computers_result}")
                    print("See you next time (:")
                    exit()
                else:
                    print("Invalid input! Try again.")
        elif choice == computers_choice:
            print(f"I choose {computers_choice} too.")
            print(f"That's a draw. No one gets a point. The result is still: {my_result}:{computers_result}")
            while True:
                ask_to_continue = input("Do you want to continue? (Yes/No): ")
                if ask_to_continue == "Yes":
                    print("Very well!")
                    break
                elif ask_to_continue == "No":
                    print(f"The final result is: {my_result}:{computers_result}")
                    print("See you next time (:")
                    exit()
                else:
                    print("Invalid input! Try again.")
        else:
            print(f"I choose {computers_choice}.")
            computers_result += 1
            print(f"Sorry you loose. {choice} beats {computers_choice}.")
            print(f"Point for me! The result is: {my_result}:{computers_result}")
            while True:
                after_loose = input("Do you want to continue? (Yes/No): ")
                if after_loose == "Yes":
                    print("Very well!")
                    break
                elif after_loose == "No":
                    print(f"The final result is: {my_result}:{computers_result}")
                    print("See you next time (:")
                    exit()
                else:
                    print("Invalid input! Try again.")

