

# # Task 4.1
# users = ['Admin', 'Designer', 'Viewer']
# # users = []
#
# if len(users) != 0:
#     for user in users:
#         if user == 'Admin':
#             print(f'Hello {user}, I hope you’re well.')
#         else:
#             print(f'Hello {user}, thank you for logging in again.')
# else:
#     print('We need to find some users!')
import math

# # Task 4.2
# side_number = int(input("Please type number from 3 to 6 of sides to find out the figure: "))
#
# if side_number == 3:
#     print('This is triangle')
# elif side_number == 4:
#     print('This is quadrilateral')
# elif side_number == 5:
#     print('This is pentagon')
# elif side_number == 6:
#     print('This is hexagon')
# else:
#     print('Number is out of boundaries. Please enter number from 3 to 6 including')

# # Task 4.3
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for n in numbers:
#     if n == 1:
#         print(f'{n}st')
#     elif n == 2:
#         print(f'{n}nd')
#     elif n == 3:
#         print(f'{n}rd')
#     else:
#         print(f'{n}th')

# # Task 4.4
# number = int(input("Please type number to find out if it's even or odd: "))
#
# if number%2 == 0:
#     print(f'Number "{number}" is even.')
# else:
#     print(f'Number "{number}" is odd.')

# # Task 4.5
# months = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31,
#           'September': 30, 'October': 31, 'November': 30, 'December': 31}
#
# month = input('Enter month to find out its number of days: ').lower().capitalize()
#
# number_of_days = months.get(month, "There are no such month")
#
# if month == 'February':
#     print(f'{month} has {number_of_days} days in common year, but in leap years it is 29 days')
# else:
#     print(f'{month} has {number_of_days} days')

# # Task 4.6
# min_year = 1900
# max_year = 3000
# year = int(input(f"Enter year from {min_year} to {max_year} to find out if it's Ordinary or Leap: "))
#
# if min_year <= year <= max_year:
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f'{year} is Leap year')
#     else:
#         print(f'{year} is Ordinary year')
# else:
#     print(f'Please enter year from {min_year} to {max_year}')

# # Task 4.7
# numbers = input("Enter numbers: ")
# listOfNumbers = list(map(int, numbers))
#
# break_num = 0
# total_sum = 0
#
# for n in listOfNumbers:
#     total_sum += n
#     if n == break_num:
#         print("Loop was broken by", break_num)
#         break
# print("Sum is", total_sum)

# # Task 4.8
# numbers = input("Enter numbers: ")
# listOfNumbers = list(map(int, numbers))
#
# while True:
#     number = int(input("Enter numbers: "))
#     if number < 10:
#         continue
#     elif number > 100:
#         break
#     else:
#         print(number)

# # Task 4.9
# while True:
#     x_str, y_str, op = input("Enter first number, second one and operator: ").split()
#     x = int(x_str)
#     y = int(y_str)
#     res = 0
#
#     try:
#         if op == '+':
#             res = x + y
#         elif op == '-':
#             res = x - y
#         elif op == '*':
#             res = x * y
#         elif op == '/':
#             res = x / y
#         elif op == 'mod':
#             res = x % y
#         elif op == 'pow':
#             res = math.pow(x, y)
#         elif op == 'div':
#             res = x // y
#         else:
#             print('Operation is not supported')
#             break
#     except ZeroDivisionError:
#         print('Division by zero!')
#         continue
#     else:
#         print(f'Result: {x_str} {op} {y_str} = {res}')

# # Task 4.10
# while True:
#     den = input("Enter denomination of hryvna's banknote: ")
#
#     if den == '1':
#         print(f'{den} hryvna - Volodymyr Velykyi')
#     elif den == '2':
#         print(f'{den} hryvnas - Yaroslav Mudryi')
#     elif den == '5':
#         print(f'{den} hryvnas - Bohdan Khmelnytskyi')
#     elif den == '10':
#         print(f'{den} hryvnas - Ivan Mazepa')
#     elif den == '20':
#         print(f'{den} hryvnas - Ivan Franko')
#     elif den == '50':
#         print(f'{den} hryvnas - Mykhailo Grushevskyi')
#     elif den == '100':
#         print(f'{den} hryvnas - Taras Shevchenko')
#     elif den == '200':
#         print(f'{den} hryvnas - Lesia Ukrainka')
#     else:
#         print(f"There is no '{den}' denomination of hryvna's banknote")

# # Task 4.11
# odd = {'a': 'black', 'b': 'white', 'c': 'black', 'd': 'white', 'e': 'black', 'f': 'white', 'g': 'black', 'h': 'white'}
# even = {'a': 'white', 'b': 'black', 'c': 'white', 'd': 'black', 'e': 'white', 'f': 'black', 'g': 'white', 'h': 'black'}
#
# while True:
#     letter_str, number_str = input("Enter letter and number for position of chess: ")
#     number = int(number_str)
#
#     if number % 2 == 0:
#         print(even.get(letter_str, 'position is missing'))
#     else:
#         print(odd.get(letter_str, 'position is missing'))

# # Task 4.12
# while True:
#     init_word = input("Enter word to check if it's palindrome: ")
#
#     if init_word == 'escape':
#         break
#
#     word = init_word.lower()
#     reversed_word = ''.join(reversed(word))
#
#     if word == reversed_word:
#         print(f"{word} == {reversed_word} - is a palindrome")
#     else:
#         print(f"{word} != {reversed_word} - is NOT a palindrome")

# # Task 4.13
# x, y = map(int, input("Enter number of rows and columns by space for multiplication table: ").split())
#
# print(f"{x}x{y}")
#
# for i in range(1, x + 1):
#     for j in range(1, y + 1):
#         print(i, 'x', j, '=', i * j)

# # Task 4.14
# from datetime import datetime, timedelta
#
# year = 2017
# day_number = int(input(f"Enter day number from the beginning of the {year} year: "))
# start = datetime(2017, 1, 1)
# new_time = start + timedelta(day_number - 1)
# print(f"{new_time.month} month {new_time.day} day")

# # Task 4.15
# decimal = input("Enter decimal number to convert it into binary: ")
# q = int(decimal)
# res = ''
# while q != 0:
#     r = q % 2
#     res = str(r) + res
#     q = q // 2
#
# print(f"'{decimal}' in Decimal is '{res}' in Binary")
#
# binary = input("Enter binary number to convert it into decimal: ")
# decimal = 0
# for digit in binary:
#     decimal = decimal * 2 + int(digit)
#
# print(f"'{binary}' in Binary is '{decimal}' in Decimal")

# # Task 4.16
# message = input("Enter message to code/decode: ")
# shift = int(input("Enter shift number to code/decode: "))
#
# new_message = ''
#
# for index, letter in enumerate(message):
#     if letter.isalpha():
#         letter_order = ord(letter)
#         new_message = new_message + chr(letter_order + shift)
#     else:
#         new_message = new_message + letter
#
# print("Coded/decoded message:", new_message)

# # Task 4.17
# import random
# def generate_password():
#     password = ''
#     length = random.randint(7, 10)
#     for i in range(length):
#         char_number = random.randint(33, 126)
#         password = password + chr(char_number)
#     return password
# print(generate_password())

# # Task 4.18
# import random
#
# a = 0
# b = 9
# limit = 3
# random_number = random.randint(a, b)
# i = 0
# while i < limit:
#     i += 1
#     num = int(input(f"Guess number from {a} to {b} including: "))
#     if random_number == num:
#         print("Congratulations! You are right!")
#         break
#     else:
#         print(f"Incorrect. Please try again. Left {limit - i} chances")

# Task 4.19