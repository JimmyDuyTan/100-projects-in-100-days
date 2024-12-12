import random

paper = '''
    _______
---'   _____)____
          _______)
          ________)
          _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(____)
'''

rock = '''
    ________
---'   _____)
       (______)
       (______)
       (____)
---.__(___)
'''

game_image = [rock, paper, scissors]

is_continue = True
while is_continue:
    # user choice are between 0, 1 , 2
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    # user choice must be 0, 1 or 2
    while user_choice < 0 or user_choice > 2:
        user_choice = int(input("You typed an invalid, please enter a valid number\n"))

    print(f"Your choice {game_image[user_choice]}")
    print("-----------------------")
    computer_choice = random.randint(0, 2)
    print(f"Computer choice {game_image[computer_choice]}")
    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif user_choice < computer_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    elif user_choice == computer_choice:
        print("It's a draw")
    # Ask if player wants to play again
    ans = input("Do you want to play again? (Y/N)\n").lower()
    #break loop if play don't play anymore
    if ans == 'n':
        is_continue = False