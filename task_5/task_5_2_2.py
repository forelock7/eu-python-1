from things import get_dict_from_tuple, get_random_thing
# Task 5.2

limit = 3
game_items = ('stone', 'scissors', 'paper')

i = 0
items_dict = get_dict_from_tuple(game_items)
while i < limit:
    i += 1
    user_choice = items_dict.get(int(input(f"Guess word from {items_dict} by index: ")))
    program_choice = get_random_thing(game_items)
    if user_choice == program_choice:
        print("Congratulations! You WON!")
        break
    else:
        print(f"Incorrect. Please try again. It was '{program_choice}'. Left {limit - i} chances")