# # Task 6.1
# init_file_path = "/Users/volodymyrchubenko/Documents/Mine/Education/Repos/eu-python-1/task_6/numbers.txt"
# sum_file_path = "/Users/volodymyrchubenko/Documents/Mine/Education/Repos/eu-python-1/task_6/sum_numbers.txt"
# with open(init_file_path, 'rt', newline='\n') as init_file:
#     lines_data = [line.rstrip('\n') for line in init_file]
#
# sum_numbers = sum(map(int, lines_data))
# print("Sum of numbers", sum_numbers)
#
# with open(sum_file_path, 'wt') as sum_file:
#     sum_file.write(str(sum_numbers))

# # Task 6.2
# file_path = "/Users/volodymyrchubenko/Documents/Mine/Education/Repos/eu-python-1/task_6/even_odd_number.txt"
# number = int(input("Enter number to find out if it's even or odd: "))
#
# def get_number_info(number):
#     if number % 2 == 0:
#         return f"{number} is even"
#     else:
#         return f"{number} is odd"
#
# message = get_number_info(number)
#
# with open(file_path, 'wt') as file:
#     file.write(message)
#
# print(message)

# # Task 6.3
# file_path = "/Users/volodymyrchubenko/Documents/Mine/Education/Repos/eu-python-1/task_6/learning_python.txt"
#
# with open(file_path, 'rt') as file:
#     lines_data = [line.rstrip('\n') for line in file]
#
# print(lines_data)

# # Task 6.4
# file_path = "/Users/volodymyrchubenko/Documents/Mine/Education/Repos/eu-python-1/task_6/learning_python.txt"
#
# with open(file_path, 'rt') as file:
#     for line in file:
#         print(line.replace('Python', 'C'))

# # Task 6.5
# file_path = "/Users/volodymyrchubenko/Documents/Mine/Education/Repos/eu-python-1/task_6/guest_book.txt"
#
# while True:
#     name = input("What's your name: ")
#     if name == 'q' or name == '':
#         break
#     message = f"Hello, {name}"
#     print(message)
#     with open(file_path, 'at') as file:
#         print(message, file=file, sep='\n')

# # Task 6.6
# file_path = "/Users/volodymyrchubenko/Documents/Mine/Education/Repos/eu-python-1/task_6/book.txt"
#
# with open(file_path, 'rt') as file:
#     text = file.read()
#
# print(text.lower().count('the'))

# # Task 6.7
# file_path = "/Users/volodymyrchubenko/Documents/Mine/Education/Repos/eu-python-1/task_6/book.txt"
# new_file_path = "/Users/volodymyrchubenko/Documents/Mine/Education/Repos/eu-python-1/task_6/formatted_text.txt"
#
# with open(file_path, 'rt', newline='\n') as file:
#     text_lines = file.readlines()
#
# with open(new_file_path, 'wt') as new_file:
#     for line in text_lines:
#         print(line.strip(), file=new_file, end=' ')

# # Task 6.8
# import re
#
# file_path = "/Users/volodymyrchubenko/Documents/Mine/Education/Repos/eu-python-1/task_6/robinson_crusoe_book.txt"
# res_file_path = "/Users/volodymyrchubenko/Documents/Mine/Education/Repos/eu-python-1/task_6/chapters.txt"
#
# chapters = []
#
# with open(file_path, 'rt') as file:
#     for line in file:
#         text = re.search("(?!.*\.)CHAPTER.*—.*", line)
#         if text:
#             chapters.append(line.strip())
#
# print('List:', chapters)
# print('Size:', len(chapters))
#
# with open(res_file_path, 'wt') as new_file:
#     for line in chapters:
#         print(line, file=new_file, end='\n')

# # Task 6.9
# file_path = "/Users/volodymyrchubenko/Documents/Mine/Education/Repos/eu-python-1/task_6/monte_cristo.txt"
#
# with open(file_path, 'rt') as file:
#     text = file.read()
#
# let = 0
# low = 0
# upp = 0
# for i in text:
#     if i.isalpha():
#         let += 1
#         if i.isupper():
#             upp += 1
#         elif i.islower():
#             low += 1
#
# print("Total number of alphabet letters:", let)
# print(f"Number of upper case alphabet letters: {upp} ({upp * 100 / let:.2f}%)")
# print(f"Number of lower case alphabet letters: {low} ({low * 100 / let:.2f}%)")

# Task 6.10
import csv
import sqlite3

file_path = "/Users/volodymyrchubenko/Documents/Mine/Education/Repos/eu-python-1/exercise_7/imdb.csv"

with open(file_path, 'rt') as freading:
    creading = csv.DictReader(freading)
    imdb = [{'title': row['title'], 'year': int(row['year']), 'rating': float(row['rating'])} for row in creading]

print(imdb)

conn = sqlite3.connect('/Users/volodymyrchubenko/Downloads/sqlite-tools-osx-x86-3430200/imdb.db')
curs = conn.cursor()
for index, item in enumerate(imdb):
    ins = 'INSERT INTO ratings (id, title, year, rating) VALUES (?, ?, ?, ?)'
    curs.execute(ins, (index, item['title'], item['year'], item['rating']))

conn.commit()

print('Order by title:')
curs.execute('SELECT * FROM ratings ORDER BY title')
for row in curs:
    print(row)

print('\nMovies with rating 8.7:')
curs.execute('SELECT * FROM ratings WHERE rating = 8.7')
for row in curs:
    print(row)
curs.close()
conn.close()