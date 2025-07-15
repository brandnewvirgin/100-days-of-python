# # random number generator
# import random
#
# random_integer = random.randint(1, 2000)
# print(random_integer)
#
# # import complex_modules
# #
# # print(complex_modules.baddest_guy)
#
# random_float = random.random()
# print(random_float)
#
# new_float = random_float * 5
# print(new_float)
#
# dice_roll = random.randint(2,12)
# print(dice_roll)
#
# import random
#
# random_sides = random.randint(0,1)
#
# if random_sides == 1:
#     print("Heads")
# else:
#     print("Tails")

# nigerian_states = ["Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross River",
#                     "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "FCT", "Gombe", "Imo", "Jigawa", "Kaduna",
#                     "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun",
#                     "Oyo", "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"]
# nigerian_states[15] = "Abuja"
#
# # nigerian_states.append("Biafra") #to add a single item to the list
# nigerian_states.extend(["Banga", "Isoko", "Tiv", "Arewa", "Middle Belt", "South South", "Oduduwa Republic"])
# print(nigerian_states[15])
# print(nigerian_states)

# #who will pay the bill
#
# # Get input from the user
# names_string = input("Enter names separated by comma and space (e.g., Alice, Bob, Charlie): ")
# # Split the string into a list of names
# names = names_string.split(", ")
#
# import random
#
# #get the total number of items on the list
# num_items = len(names)
# #generate random numbers between 0 and the last index
# random_choice = random.randint(0, num_items - 1)
# #pick out random person from list using random number
# person_who_pays = names[random_choice]
# print(person_who_pays + " is going to pay for the meal today!")

# # dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches". "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
#
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Sinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen)

# #treasure map code
#
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# #choose the position you want to change and format it to lowercase
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# numbers_index = int(position[1]) - 1
# map[numbers_index][letter_index] = "X"
#
# print(f"{line1}\n{line2}\n{line3}")

# #rock, paper and scissors game
#
# import random
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# #create a list to store the choices
# choices = [choice.lower() for choice in ["Rock", "Paper", "Scissors"]]
# #randomise all three outcomes
# rock_outcome = random.random()
# paper_outcome = random.random()
# scissors_outcome = random.random()
# #store user choice
# user_choice = input("rock, paper, or scissors? ")
# #store the computer choice
# computer_choice = random.choice(choices)
# #set conditions for the final outcomes
# if user_choice == rock_outcome and computer_choice == paper_outcome:
#     print("You lose! Paper wraps rock")
# elif user_choice == rock_outcome and computer_choice == scissors_outcome:
#     print("You lose! Scissors cut paper")
# else:
#     print("Invalid choice")

# #rock, paper, and scissors game
# import random
#
# # ASCII art for rock, paper, scissors
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# # Store choices in a list
# choices = ["rock", "paper", "scissors"]
#
# # Get user input
# user_choice = input("Choose: rock, paper, or scissors? ").lower()
#
# # Validate user input
# if user_choice not in choices:
#     print("Invalid choice!")
# else:
#     # Get computer choice
#     computer_choice = random.choice(choices)
#
#     # Print both choices using ASCII art
#     def print_choice(choice):
#         if choice == "rock":
#             print(rock)
#         elif choice == "paper":
#             print(paper)
#         elif choice == "scissors":
#             print(scissors)
#
#     print("\nYou chose:")
#     print_choice(user_choice)
#
#     print("Computer chose:")
#     print_choice(computer_choice)
#
#     # Determine the winner
#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif (
#         (user_choice == "rock" and computer_choice == "scissors") or
#         (user_choice == "paper" and computer_choice == "rock") or
#         (user_choice == "scissors" and computer_choice == "paper")
#     ):
#         print("You win!")
#     else:
#         print("You lose!")

#rock, paper, and scissors game
import random

# ASCII art for rock, paper, scissors
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
---'    ____)____
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
#record the game images in a list
game_images = [rock, paper, scissors]
#create input for user choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose")
else:
    print(game_images[user_choice])
    #create computer random choice
    computer_choice = random.randint(0, 2)
    #testrun the code
    print("Computer chose:")
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("Ypu win")
    elif computer_choice == user_choice:
        print("It's a draw")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
