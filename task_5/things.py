import random
# Task 5.2
def get_random_thing(items):
    return random.choice(items)

def get_dict_from_tuple(items):
    return {index: word for index, word in enumerate(items)}