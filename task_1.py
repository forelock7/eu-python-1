# # Task 1.1
# a = 'Hello, World'
# print(a)
# a = 'By, Human being'
# print(a)
import math

# # Task 1.2
# name = 'Volodymyr'
# print('Hello, {}, would you like to learn some Python today?'.format(name))

# # Task 1.3
# famous_person = 'Steve Jobs'
# message = '{} once said, \"Your time is limited, so don\'t waste it living someone else\'s life.\"'.format(famous_person)
# print(message)

# # Task 1.4
# username = """  Volodymyr
# """
# print("---Start---")
# print(username)
# print(username.lstrip())
# print(username.rstrip())
# print(username.strip())
# print("---End---")

# # Task 1.5
# print("Volodymyr Chubenko")
# print("Ukraine")
# print("31100")
# print("Starokostiantyniv")
# print("Ostrozkoho street")
# print("1/1")
# print("app. 1")

# # Task 1.6
# distance = int(input('Please enter the distance: '))
# print('{:.2f} km(s)'.format(distance))
# print('{:.2f} inches'.format(distance * 39370.0787))
# print('{:.2f} feet'.format(distance * 3280.8399))
# print('{:.2f} miles'.format(distance * 0.621371192))
# print('{:.2f} yards'.format(distance * 1093.6133))

# # Task 1.7
# conference_beginning = int(input("Please enter calendar day of the conference beginning: "))
# conference_end = int(input("Please enter calendar day of the conference end: "))
# dur = conference_end - conference_beginning
# print("The conference was held during h/min/sec: {0:<10} / {1:<10} / {2:<10}!".format(dur * 24, dur * 24 * 60, dur * 24 * 60 * 60))

# # Task 1.8
# # Takes temperature in C
# temperature_in_c = float(input('Please enter the temperature in C for converting: '))
# # Calculates temperature into F
# temperature_in_f = 32 + temperature_in_c * 9/5
# # Calculates temperature into K
# temperature_in_k = temperature_in_c + 273.15
# # Prints out calculated temperatures
# print('{0:^10.2f} {1:^10.2f} {2:^10.2f}'.format(temperature_in_c, temperature_in_f, temperature_in_k))

# # Task 1.9
# number = int(input("Please enter an integer of 4 digits: "))
# number_string = str(number)
# n0 = number_string[0]
# n1 = number_string[1]
# n2 = number_string[2]
# n3 = number_string[3]
# print(f'{n0} + {n1} + {n2} + {n3} = {int(n0) + int(n1) + int(n2) + int(n3)}')

# # Task 1.10
# # Beijing coordinates
# beijing_x = math.radians(39.9075000)
# beijing_y = math.radians(116.3972300)
# # Kyiv coordinates
# kyiv_x = math.radians(50.4546600)
# kyiv_y = math.radians(30.5238000)
# # calculates distance between cities
# distance = 6371.032 * math.acos(math.sin(beijing_x) * math.sin(kyiv_x) + math.cos(beijing_x) * math.cos(kyiv_x) * math.cos(beijing_y - kyiv_y))
# # Outputs distance
# print(f'Distance between Beijing and Kyiv is: {distance:>10.3f}')
# london_x = math.radians(51.50853)
# london_y = math.radians(-0.12574)
# distance2 = 6371.032 * math.acos(math.sin(london_x) * math.sin(kyiv_x) + math.cos(london_x) * math.cos(kyiv_x) * math.cos(london_y - kyiv_y))
# print(f'Distance between London and Kyiv is: {distance2:>10.3f}')

# Task 1.11
# Updated Task 1.6
# Updated Task 1.7
# Updated Task 1.8
# Updated Task 1.9

# Task 1.12
# Updated Task 1.8
# Updated Task 1.10