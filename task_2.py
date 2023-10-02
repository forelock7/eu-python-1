# # Task 2.1
# countries = ["Ukrainian", "French", "Bulgarian", "Norwegian", "Latvian"]
# print("Initial list: ", countries)
# print("New sorted list: ", sorted(countries))
# print("Initial list: ", countries)
# countries.reverse()
# print("Reversed list: ", countries)
# countries.sort()
# print("Sorted list: ", countries)

# # Task 2.2
# numbers = input("Enter numbers separated by a space: ")
# listOfNumbers = list(map(int, numbers.split(' ')))
# print("List of numbers: ", listOfNumbers)
# print("Sum of list items: ", sum(listOfNumbers))

# # Task 2.3
# cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
# size = len(cities)
# mess = ''
#
# for index, value in enumerate(cities):
#     mess += value
#     if index < size - 2:
#         mess += ', '
#     elif index == size - 2:
#         mess += ' and '
#
# print(mess)

# # Task 2.4
# numbers = input("Enter 5 numbers separated by a space: ")
# listOfNumbers = list(map(int, numbers.split(' ')))
# sortedList = sorted(listOfNumbers, reverse=True)
# print('Origin list: ', listOfNumbers)
# print('Sorted list: ', sortedList)
# print('Merged number: ', ''.join(map(str, sortedList)))

# # Task 2.5
# sportTypes = ['football', 'basketball', 'hokey', 'fencing', 'running']
# print("Initial list: ", sportTypes)
# print("New sorted list: ", sorted(sportTypes))
# sportTypes.reverse()
# print("Reversed list: ", sportTypes)
# sportTypes.sort()
# print("Sorted list: ", sportTypes)
# print("Number of sport's types: ", len(sportTypes))
# print("Ssport's types: ", ', '.join(sportTypes))

# # Task 2.6
# postfixExpression = '2+4-6*7/3'
# numbers = ''
# signs = ''
# for token in postfixExpression:
#     if token.isnumeric():
#         numbers += token
#         print(numbers)
#     else:
#         signs += token
#         print(signs)
# print('Results: ', numbers + signs)
