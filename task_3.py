# # Task 3.1
# network_prot = {'UDP': 'one of the core communication protocols of the Internet protocol suite used to send messages '
#                    '(transported as datagrams in packets) to other hosts on an Internet Protocol (IP) network',
#             'TCP': 'one of the main protocols of the Internet protocol suite. It originated in the initial network '
#                    'implementation in which it complemented the Internet Protocol (IP)',
#             'IP': 'the network layer communications protocol in the Internet protocol suite for relaying datagrams '
#                   'across network boundaries. Its routing function enables internet working, and essentially establishes '
#                   'the Internet'}
# for term, definition in network_prot.items():
#     print(f'{term}:\n\t{definition}')

# # Task 3.2
# rivers = {'Amazon': 'South America', 'Dnipro': 'East Europe', 'Nile': 'South Africa'}
# for river, region in rivers.items():
#     print(f'The {river} runs through {region}.')

# # Task 3.3
# inventors = {'Java': 'James Gosling', 'Java Script': 'Brendan Eich', 'Python': 'Guido van Rossum', 'C#': 'Anders Hejlsberg'}
# for lang, person in inventors.items():
#     print(f'My favorite programming language is {lang}. It was created by {person}.')
# del inventors['C#']
# print(inventors)

# # Task 3.4
# english_german_dict = {'stork': 'storch', 'hawk': 'falke', 'woodpecker': 'specht', 'owl': 'eule'}
# print(english_german_dict.get('owl'))
# english_german_dict['horse'] = 'pferd'
# english_german_dict['mouse'] = 'maus'
# print('dictionary: ', english_german_dict)
# print('keys list: ', list(english_german_dict.keys()))
# print('values list: ', list(english_german_dict.values()))

# # Task 3.5
# jack = {'Alex': 'dog'}
# sonia = {'Anna': 'cat'}
# pets = [jack, sonia]
# print(pets)
# for p in pets:
#     for owner, pet_type in p.items():
#         print(f'{owner} is the owner of a pet - a {pet_type}.')

# # Task 3.6
# morse = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
#           'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
#           'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
#           '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
#           '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}
# words = input('Please type something to convert it into morse: ').upper();
# translated = ''
# for w in words:
#     translated += morse.get(w, '?')
# print('Translation in morse: ', translated)

# # Task 3.7
# subjects = {'science': {'physics': ['nuclear physics', 'optics', 'thermodynamics'], 'computer science': {}, 'biology': {}},
#             'humanities': {}, 'public': {}}
# print(subjects['science'])
# print(subjects['science']['physics'])

# # Task 3.8
# cities = {'Kyiv': {'country': 'Ukraine', 'population': 2952301, 'fact': 'It was founded in 482'},
#           'London': {'country': 'Greate Britain', 'population': 8799800, 'fact': 'It stands on the River Thames'},
#           'New York': {'country': 'USA', 'population': 8804190, 'fact': 'It is the most populous city in the United States'}}
#
# for city, info in cities.items():
#     print(f"{city} is in {info.get('country')} and has {info.get('population')} population.\n\tSome interesting fact: {info.get('fact')}")

# # Task 3.9
# teams = {'LA Lakers': [23, 20, 2, 1, 62], 'NY Knicks': [23, 15, 5, 3, 50], 'Detroit Pistons': [20, 4, 8, 8, 20]}
#
# for team, stat in teams.items():
#     stat_str = [str(int) for int in stat]
#     print(f"{team.upper()} {' '.join(stat_str)}")

# # Task 3.10
# things = {'key': 3, 'mace': 1, 'gold coin': 24, 'lantern': 1, 'stone': 10}
# print('Equipment:')
# total = 0
# for attr, num in things.items():
#     total += num
#     print(f"{num} {attr}")
# print('Total number of things:', total)