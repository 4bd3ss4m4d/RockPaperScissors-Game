import random

# Rock Paper Scissors Game
print("Welcome to the Rock Paper Scissors Games.\n")

#INSERT ROCK PAPER SCISSORS ASCII ART
rock = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#
choices = [rock, paper, scissors]

choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors: \n"))

if choice > 2:
    print("Wrong input! try again.\n")
else :
    #
    print(f"What you've chosen : \n`\n")
    print(choices[choice])
    print("\n\n")

#
    random_choice = random.randint(0, 2)

#


#
    print("The computer has chosen: \n\n")
    print(choices[random_choice])
    print("\n\n")

#
    if choice == 0:
        if random_choice == 0:
            print("Its a draw!\n")
        elif random_choice == 1:
            print("The computer wins!\n")
        elif random_choice == 2:
            print("You win! \n")
    elif choice == 1:
        if random_choice == 0:
            print("You win!\n")
        elif random_choice == 1:
            print("Its a draw!\n")
        elif random_choice == 2:
            print("The computer wins!\n")
    elif choice == 2:
        if random_choice == 0:
            print("The computer wins!\n")
        elif random_choice == 1:
            print("You win!\n")
        elif random_choice == 2:
            print("Its a draw!\n")