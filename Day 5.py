#fruits
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
#     # print(fruits)
# print(fruits)
#
# #girlfriends
#
# girlfriends = ["Shalewa", "Vanessa", "Omotola", "Barbara", "Ugonna", "Amara"]
# for babe in girlfriends:
#     print(babe)
#     print(babe + " was my ex")

# # Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     total_height = student_heights += 0
#     print(student_heights)

# # Input a list of student heights as strings, split by spaces
# student_heights = input().split()
#
# # Convert each string in the list to an integer
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#
# # Initialize a variable to hold the total height
# total_height = 0
#
# # Add each student's height to the total
# for height in student_heights:
#     total_height += height
#
# # Print the total combined height
# print(f"Total height = {total_height}")
#
# # Initialize a variable to count the number of students
# number_of_students = 0
#
# # Count how many students are in the list
# for student in student_heights:
#     number_of_students += 1
#
# # Print the total number of students
# print(f"Number of students = {number_of_students}")
#
# # Calculate the average height and round it to the nearest whole number
# average_height = round(total_height / number_of_students)
#
# # Print the calculated average height
# print(f"The average height = {average_height}")

# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# #create a variable for the highest score
# highest_score = 0
# #create a variable for the scores
# highest_score = student_scores[0]
# for score in highest_score:
#   #comparee the scores
#   if score > highest_score:
#     highest_score = score
# #print result
# print(f"Your highest score is {highest_score}")

# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
#
# #assign a variable to highest score
# highest_score = 0
# for score in student_scores:
#   #compare the scores
#   if score > highest_score:
#     highest_score = score
#
# #print highest score
# print((f"Your highest score in the class is {highest_score}"))

# #for loop in range
# for number in range(1, 11, 3):
#  print(number)

# #calculate the sum of numbers between 1 and 100
# total = 0
# for number in range(1, 101):
#   total += number
# print(total)

# #ask the user to select a number
# target = int(input()) # Enter a number between 0 and 1000
# #store the total number in a variable and assign the value zero to it
# total = 0
# #use the for long to loop the range of the selected numbers
# for number in range(1, target):
#   #check for even numbers within the range
#   if number %2 == 0:
#     #calculate all even numbers
#     total += number
# print(f"The total number is: {total}")

# target = int(input()) # Enter a number between 0 and 1000
# even_sum = 0
# #accumulate even_sum here
# for number in range(2, target + 1, 2):
#   #test run the code to check for even numbers
#   even_sum += number
#   # print(number)
# print(even_sum)

# #or
#
# alternative_sum = 0
# for number in range(1, target +1):
#   if number % 2 == 0:
#     alternative_sum += number
# print(alternative_sum)

# #FizzBuzz game
# list = range(1, 100+1)
# number_choice = int(input("Choose a number between 1 and 100\n"))
# if number_choice % 3 == 0 and number_choice % 5 == 0:
#   print("Fizz")
#   elif number_choice % 5 == 0:
#   print("Buzz")
#   elif number_choice % 3 == 0:
#   print("FizzBuzz")
# else:
#   print(number_choice)

# list = int(input("Call out a random number"))
# for number in range(1, list +1, 3):
#   print("Fizz")
# for number in range(1, list  +1, 5):
#   print("Buzz")

# #FizzBuzz Game
# #set a variable for the target number
# target = 100
# #set a range for the variable
# for number in range(1, target +1):
#     #use if, elif and else statements to check for prerequisite conditions
#     #check for numbers that are divisible by 3 and 5 first
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# #password generator project
# import random
# # Letters (all uppercase and lowercase a-z)
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#
# # Numbers (as strings)
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
# # Or if you want numbers as integers
# # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # Symbols (common special characters)
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# #print welcome statement
# print("Welcome to thePyPassword Generator")
#
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_numbers = int(input(f"How many numbers would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like in your password?\n"))
#
# for letter in nr_letters:
#     letter = nr_letters.random(input())
#     print(letter)
# for number in nr_numbers:
#     number = nr_numbers.randint(input())
# for symbol in nr_symbols:
#     symbol = nr_symbols.randit(input())
#
# password = letter + number + symbol
# print(password)

#password generator project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to thePyPassword Generator")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like in your password?\n"))

# #easy level
# password = ""
# #nr_letters = 4
# for char in range(1, nr_letters + 1):
#     #1 - 4
#     # random_char = random.choice(letters)
#     # print(random_char)
#     # password += random_char
#     # print(password)
#     password += random.choice(letters)
#
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
#
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#     print(f"Your password is {password}")

#hard level

password_list = []
for char in range(1, nr_letters + 1):
    #1 - 4
    # random_char = random.choice(letters)
    # print(random_char)
    # password += random_char
    # print(password)
    password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

print(password_list)

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is is: {password}")