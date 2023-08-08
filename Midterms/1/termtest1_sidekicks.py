# ENDG 233 F21 - Term Test #1 Written Response (9 marks)
# Omar Ahmed

# The following program accepts the input of a movie sidekick and searches a dictionary database to find their corresponding movie title.
# If the sidekick is in the database, the movie title is printed.
# If the sidekick is not in the database, they are added, along with their input movie title.
# The program will also print out the number of sidekicks currently in the database each time a transaction is completed.
# The program must also print out a list of all movie titles in the database without repeating duplicate titles.
# The main code is already implemented. 
# A screenshot of example input/output has been provided.

# TASKS:
# Complete the functions print_movies and lookup_movie. Read through their docstrings to learn more about the functions.
# One line of functionality is missing in the main section. Write a single line of code at the designated position to complete the logic.
# You may not modify any of the given code.


def print_movies(sidekicks):
    print(set(list(sidekicks.values())))
    """
    Prints all unique titles currently held in the dictionary. No titles are duplicated in the printout.

    Arguments:
    sidekicks -- dictionary mapping a sidekick name string to a movie title string

    Returns:
    None
    
    """

def lookup_movie(char_name, sidekick_dict):
    if char_name in sidekick_dict:
        return sidekick_dict[char_name]
    else:
        return 'Sidekick not found'
    """
    Searches the provided dictionary to find the movie title that matches the desired sidekick name.

    Arguments:
    char_name -- string representing the sidekick name input by the user
    sidekick_dict -- dictionary mapping a sidekick name string to a movie title string

    Returns:
    Returns the corresponding movie title string if a match is found, otherwise returns the string 'Sidekick not found'
    
    """



# Starting database defintion.
sidekicks = {
    'Sebastian' : 'The Little Mermaid',
    'Pascal' : 'Tangled',
    'Flounder' : 'The Little Mermaid',
    'Slinky' : 'Toy Story',
    'Merriweather' : 'The Sleeping Beauty',
    'Olaf' : 'Frozen',
    'Charlotte' : 'The Princess and the Frog',
    'Bruce' : 'Finding Nemo',
    'Mushu' : 'Mulan',
    'Genie' : 'Aladdin',
    'Rex' : 'Toy Story',
    'Louis' : 'The Princess and the Frog',
    'Dante' : 'Coco',
    'Abu' : 'Aladdin',
    'Edna' : 'The Incredibles',
    'Iago' : 'Aladdin',
    'Ray' : 'The Princess and the Frog'
}

# Initialize sidekick input
input_sidekick = -1

# Continuous input loop
while(input_sidekick != '0'):
    print('\nThere are {} sidekicks stored in the database.'.format(len(sidekicks)))
    input_sidekick = input('Enter the name of a sidekick or select 0 to end: ')

    if input_sidekick != '0':
        lookup_result = lookup_movie(input_sidekick, sidekicks)    # Call the lookup_movie function

        if(lookup_result != 'Sidekick not found'):
            print('{} is a sidekick in the movie "{}".'.format(input_sidekick, lookup_result))    # If sidekick is found, print their movie title
        else:
            new_movie = input('Sidekick entry not found. Please enter the name of the sidekick\'s movie: ')
            sidekicks[input_sidekick] = new_movie
            print('New sidekick added.')

        print('\nThere are {} sidekicks stored in the database.'.format(len(sidekicks)))
        print('The current list of movies in the database is: ')
        print_movies(sidekicks)     # Call the print_movies function


# Successful execution will be worth an additional 3 marks.
