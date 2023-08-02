def print_movies(sidekicks):
    print(set(list(sidekicks.values())))

def lookup_movie(char_name, sidekick_dict):
    if char_name in sidekick_dict:
        return sidekick_dict[char_name]
    else:
        return 'Sidekick not found'

sidekicks[input_sidekick] = new_movie

print (new_movie)
