# final_project.py
#Omar Ahmed
# A terminal-based application to process and plot data based on given user input and provided csv files

import numpy as np                                  # Imports the module numpy
import matplotlib.pyplot as plt                     # Imports the module matplotlib

class Area:
    '''A class used to create an Area object.

        Attributes:
            state (str): String that represents the state's name
            state_code (str): String that represents the states's code
            region(str): String that represents the state's region
    '''
    def __init__(self, state, state_code, region):
        self.state = state 
        self.state_code = state_code
        self.region = region

    def print_stats(self):
        '''A function that prints the name, the code, and the region of the state requested.

        Parameters: None
        Return: None

        '''
        print("State: {0}\nState Code: {1}\nRegion: {2}".format(self.state, self.state_code, self.region))


def get_index(arr, state):
    '''A function that returns the index of a state in a certain array.

    Parameters:
        arr -- string representing the array which will be analyzed.
        state -- string representing the state wich we want to know the index in a certain array.

    Return Values:
        index_array -- The function returns an integer (the index of the state in the array).
    '''
    index_array = 0
    for i in range(0, len(arr)):
        if state == arr[i][1]:
            index_array = i
    return index_array

def get_list_from_array_column(arr, column):
    '''A function that returns a list containing all the values of a certain column in an array.

    Parameters:
        arr -- string representing the array which will be analyzed.
        column -- int representing the column wich we want the items to be turned into a list.

    Return Values:
        list -- list containing all the values of a certain column in the array requested.
    '''
    list = []
    for i in range(0, len(arr)):
        item = arr[i][column]
        if item.isnumeric() is True:
            list.append(int(arr[i][column]))
        else:
            list.append(arr[i][column])
    return list


array_unemployment = np.genfromtxt('unemployment.csv', delimiter=',', skip_header=1, dtype = str)                       # Imports the CSV file 'unemployment.csv' as a numpy array
array_covid = np.genfromtxt('covid.csv', delimiter=',', skip_header=1, dtype = str)                                     # Imports the CSV file 'covid.csv' as a numpy array
array_state_demographics = np.genfromtxt('state_demographics.csv', delimiter=',', skip_header=1, dtype = str)           # Imports the CSV file 'state_demographics.csv' as a numpy array
array_states_to_region = np.genfromtxt('states_to_region.csv', delimiter=',', skip_header=1, dtype = str)               # Imports the CSV file 'states_to_region.csv' as a numpy array
array_per_capita = np.genfromtxt('state_per_capita.csv', delimiter=',', skip_header=1, dtype = str)                     # Imports the CSV file 'state_per_capita.csv' as a numpy array

list_of_states = get_list_from_array_column(array_states_to_region, 0)                                                  # Creates a list with all the values from column 0 of the array 'array_states_to_region' by calling the function 'get_list_from_array_column'
list_of_state_codes = get_list_from_array_column(array_states_to_region, 1)                                             # Creates a list with all the values from column 1 of the array 'array_states_to_region' by calling the function 'get_list_from_array_column'
list_of_regions = get_list_from_array_column(array_states_to_region, 2)                                                 # Creates a list with all the values from column 2 of the array 'array_states_to_region' by calling the function 'get_list_from_array_column'


def main():
    
    print('\nEconomy and Covid: How Covid Economically Impacted the US States.\n')                                      # Print information about the program to the user
    print('This program provides information about the Covid and the economic statistics in the United States')         # Prints information about the program to the user
    

    while True:                                                                                                         # While loop that serves to ask the user for another input in case that the previous input was not valid
        
        user_area_request = input('Please, select an US State (You can select the State either by typing the full name of the State or the state code): ')      # Asks the user for the name of an US State
    
        if user_area_request.lower().strip().title() in array_states_to_region[:,0]:                                            # Analyzes if the user input is valid in case the user inputed the name of the state
            state_requested = user_area_request.lower().strip().title()                                                         # Formats the user input
            state_code_requested = list_of_state_codes[list_of_states.index(user_area_request.lower().strip().title())]         # Gets the code of the state requested by the user
            region_requested = array_states_to_region[list_of_states.index(user_area_request.lower().strip().title())][2]       # Gets the region of the state requested by the user
        
            break                                                                                                               # Breaks the while loop

        elif user_area_request.upper() in array_states_to_region[:,1]:                                                          # Analyzes if the user input is valid in case the user inputed the code of the state
            state_code_requested = user_area_request.upper()                                                                    # Formats the user input
            state_requested = list_of_states[list_of_state_codes.index(user_area_request.upper())]                              # Gets the name of the state requested by the user
            region_requested = array_states_to_region[list_of_state_codes.index(user_area_request.upper())][2]                  # Gets the region of the state requested by the user

            break                                                                                                               # Breaks the while loop
        
        else:
            print('You must enter a valid State or state code')                                                                 # Prints an error message to the user in case the user input is invalid
            continue                                                                                                            # Goes back to the beginning of the while loop


    print("\n***Requested Area Information***\n") 
           
 
    area_requested = Area(state_requested, state_code_requested, region_requested)                                              # Creates the variable "area_requested" with the class "Area"
    area_requested.print_stats()                                                                                                # Prints the name of the state, the code of the state, and the region of the state by calling the method 'print_stats' of the class 'Area'

    while True:                                                                                                                 # While loop that serves to ask the user for another input in case that the previous input was not valid

        user_topic = input('\nChoose a letter corresponding to a topic:\n    A - Covid\n    B - Economics\n    ')               # Asks the user for a topic
        user_topic = user_topic.upper()                                                                                         # Formats the user input

        if user_topic == 'A' or user_topic == 'B':                                                                              # Analyzes if the user input is valid
            print("\n***Requested Area Statistics***\n")
            break                                                                                                               # Breaks the while loop

        else:
            print('You must enter a letter that corresponds to a topic')                                                        # Prints an error message to the user in case the user input is invalid                                         
            continue                                                                                                            # Goes back to the beginning of the while loop

    index_array_covid = get_index(array_covid, state_requested)                                                                 # Gets the index of the state requested by the user in the array 'array_covid' by calling the function 'get_index'
    index_array_demographics = get_index(array_state_demographics, state_requested)                                             # Gets the index of the state requested by the user in the array 'array_state_demographics' by calling the function 'get_index'
    index_array_per_capita = get_index(array_per_capita, state_requested)                                                       # Gets the index of the state requested by the user in the array 'array_per_capita' by calling the function 'get_index'    
    index_array_unemployment = get_index(array_unemployment, state_requested)                                                   # Gets the index of the state requested by the user in the array 'array_unemployment' by calling the function 'get_index'

    if user_topic == 'A':                                                                                                       # If the user chose the topic 'A - Covid', the program presents the user with Covid information about the state requested

        number_of_cases = int(array_covid[index_array_covid][3])                                                                # Creates a variable with the number of covid cases in the state requested by the user
        number_of_deaths = int(array_covid[index_array_covid][4])                                                               # Creates a variable with the number of covid deaths in the state requested by the user

        if array_covid[index_array_covid][5] != '':                                                                             # Checks if the array 'array_covid' have data concerning the number of confirmed cases of the state requested by the user
            number_of_confirmed_cases = int(array_covid[index_array_covid][5])                                                  # In case the array 'array_covid' has data about the number of confirmed cases, it assigns the variable 'number_of_confirmed_cases' to the actual number of confirmed cases
        else:
            number_of_confirmed_cases = 'No Data'                                                                               # In case the array 'array_covid' does not have data about the number of confirmed cases, it assigns the variable 'number_of_confirmed_cases' to the string 'No Data'

        if array_covid[index_array_covid][6] != '':                                                                             # Checks if the array 'array_covid' have data concerning the number of confirmed deaths of the state requested by the user
            number_of_confirmed_deaths = int(array_covid[index_array_covid][6])                                                 # In case the array 'array_covid' has data about the number of confirmed deaths, it assigns the variable 'number_of_confirmed_deaths' to the actual number of confirmed deaths
        else:
            number_of_confirmed_deaths = 'No Data'                                                                              # In case the array 'array_covid' does not have data about the number of confirmed deaths, it assigns the variable 'number_of_confirmed_deaths' to the string 'No Data'       
        
        if array_covid[index_array_covid][7] != '':                                                                             # Checks if the array 'array_covid' have data concerning the number of probable cases of the state requested by the user
            number_of_probable_cases = array_covid[index_array_covid][7]                                                        # In case the array 'array_covid' has data about the number of probable cases, it assigns the variable 'number_of_probable_cases' to the actual number of probable cases
        else:
            number_of_probable_cases = 'No Data'                                                                                # In case the array 'array_covid' does not have data about the number of probable cases, it assigns the variable 'number_of_probable_cases' to the string 'No Data'                                                         

        if array_covid[index_array_covid][8] != '':                                                                             # Checks if the array 'array_covid' have data concerning the number of probable deaths of the state requested by the user
            number_of_probable_deaths = array_covid[index_array_covid][8]                                                       # In case the array 'array_covid' has data about the number of probable deaths, it assigns the variable 'number_of_probable_deaths' to the actual number of probable cases
        else:
            number_of_probable_deaths = 'No Data'                                                                               # In case the array 'array_covid' does not have data about the number of probable deaths, it assigns the variable 'number_of_probable_deaths' to the string 'No Data'                                                     
        
        print('Data Last Updated On: {}\n'.format(array_covid[index_array_covid][0]))                                           # Prints the date when the covid data was last updated
        print('Total Number of Cases: {}'.format(number_of_cases))                                                              # Prints total number of cases
        print('Total Number of Deaths: {}\n'.format(number_of_deaths))                                                          # Prints total number of deaths
        print('Number of Confirmed Cases: {}'.format(number_of_confirmed_cases))                                                # Prints number of confirmed cases
        print('Number of Confirmed Deaths: {}'.format(number_of_confirmed_deaths))                                              # Prints number of confirmed deaths
        print('Number of Probable Cases: {}'.format(number_of_probable_cases))                                                  # Prints number of probable cases
        print('Number of Probable Deaths: {}\n'.format(number_of_probable_deaths))                                              # Prints number of probable deaths

        population = int(array_state_demographics[index_array_demographics][4])                                                 # Gets the population of 2020 of the state requested by the user

        percentage_of_population_infected = ((number_of_cases)/(population))*100                                                # Calculates the percentage of the population that got Covid in the state requested by the user
        percentage_of_deaths_in_relation_to_population = (number_of_deaths/population)*100                                      # Calculates the percentage of deaths in the state requested by the user in relation to the population of the same state

        print('Percentage of Population Infected by Covid: {:.2f}%'.format(percentage_of_population_infected))                  # Prints the percentage of the population that got Covid in the state requested by the user
        print('Percentage of Deaths in Relation to Population: {:.2f}%'.format(percentage_of_deaths_in_relation_to_population)) # Prints the percentage of deaths in the state requested by the user in relation to the population of the same state


        print("\n***Comparison to Other States***\n")


        list_covid_cases = get_list_from_array_column(array_covid, 3)                                                           # Gets a list with all the items from column 3 of the array 'array_covid' by calling the function 'get_list_from_array_column'

        array_covid_cases = np.array([list_covid_cases])                                                                        # Converts the list 'list_covid_cases' into a numpy array
        state_most_cases_num_cases = np.max(array_covid_cases)                                                                  # Gets the biggest number from the array 'array_covid_cases'
        state_most_cases = array_covid[list_covid_cases.index(state_most_cases_num_cases)][1]                                   # Gets the name of the state with the most number of covid cases
        state_least_cases_num_cases = np.min(array_covid_cases)                                                                 # Gets the smallest number from the array 'array_covid_cases'
        state_least_cases = array_covid[list_covid_cases.index(state_least_cases_num_cases)][1]                                 # Gets the name of the state with the least number of covid cases


        list_covid_deaths = get_list_from_array_column(array_covid, 4)                                                          # Gets a list with all the items from column 4 of the array 'array_covid' by calling the function 'get_list_from_array_column'

        array_covid_deaths = np.array([list_covid_deaths])                                                                      # Converts the list 'list_covid_deaths' into a numpy array
        state_most_deaths_num_deaths = np.max(array_covid_deaths)                                                               # Gets the biggest number from the array 'array_covid_deaths'
        state_most_deaths = array_covid[list_covid_deaths.index(state_most_deaths_num_deaths)][1]                               # Gets the name of the state with the most number of covid deaths
        state_least_deaths_num_deaths = np.min(array_covid_deaths)                                                              # Gets the smallest number from the array 'array_covid_deaths'
        state_least_deaths = array_covid[list_covid_deaths.index(state_least_deaths_num_deaths)][1]                             # Gets the name of the state with the least number of covid deaths



        if number_of_cases == state_most_cases_num_cases:                                                                       # In case the state requested by the user is the state with most number of Covid cases, a graph comparing the state requested by the user and the state with least number of cases is plotted

            print(state_requested, 'is the state with most number of cases!')                                                   # Prints a message to the user informing that the state requested is the state with most number of Covid cases
            plt.bar(state_requested, number_of_cases, label = 'State Requested', color = 'y')                                   # Plots the information about the state requested
            plt.bar(state_least_cases, state_least_cases_num_cases, label = 'State With Least Number of Cases', color = 'g')    # Plots the information about the state with least number of cases
            plt.legend(shadow = True)                                                                                           # Adds a legend to the graph
            plt.ylabel('Number of Cases')                                                                                       # Adds a label to the y-axis of the graph
            plt.xlabel('State')                                                                                                 # Adds a label to the x-axis of the graph
            plt.title('Comparison With Number of Cases:')                                                                       # Adds a title to the graph
            plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)                                                 # Formats the ticks in the x-axis
            plt.show()                                                                                                          # Shows the graph to the user

        elif number_of_cases == state_least_cases_num_cases:                                                                    # In case the state requested by the user is the state with least number of Covid cases, a graph comparing the state requested by the user and the state with most number of cases is plotted
            
            print(state_requested, 'is the state with least number of cases!')                                                  # Prints a message to the user informing that the state requested is the state with least number of Covid cases
            plt.bar(state_most_cases, state_most_cases_num_cases, label = 'State With Most Number of Cases', color = 'r')       # Plots the information about the state with most number of cases     
            plt.bar(state_requested, number_of_cases, label = 'State Requested', color = 'y')                                   # Plots the information about the state requested
            plt.legend(shadow = True)                                                                                           # Adds a legend to the graph
            plt.ylabel('Number of Cases')                                                                                       # Adds a label to the y-axis of the graph
            plt.xlabel('State')                                                                                                 # Adds a label to the x-axis of the graph
            plt.title('Comparison With Number of Cases:')                                                                       # Adds a title to the graph
            plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)                                                 # Formats the ticks in the x-axis  
            plt.show()                                                                                                          # Shows the graph to the user

        else:
            plt.bar(state_most_cases, state_most_cases_num_cases, label = 'State With Most Number of Cases', color = 'r')       # Plots the information about the state with most number of cases 
            plt.bar(state_requested, number_of_cases, label = 'State Requested', color = 'y')                                   # Plots the information about the state requested
            plt.bar(state_least_cases, state_least_cases_num_cases, label = 'State With Least Number of Cases', color = 'g')    # Plots the information about the state with least number of cases
            plt.legend(shadow = True)                                                                                           # Adds a legend to the graph
            plt.ylabel('Number of Cases')                                                                                       # Adds a label to the y-axis of the graph
            plt.xlabel('State')                                                                                                 # Adds a label to the x-axis of the graph
            plt.title('Comparison With Number of Cases:')                                                                       # Adds a title to the graph
            plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)                                                 # Formats the ticks in the x-axis
            plt.show()                                                                                                          # Shows the graph to the user


        if number_of_deaths == state_most_deaths_num_deaths:                                                                     # In case the state requested by the user is the state with most number of Covid deaths, a graph comparing the state requested by the user and the state with least number of Covid deaths is plotted

            print(state_requested, 'is the state with most number of deaths!')                                                   # Prints a message to the user informing that the state requested is the state with most number of Covid deaths
            plt.bar(state_requested, number_of_deaths, label = 'State Requested', color = 'y')                                   # Plots the information about the state requested
            plt.bar(state_least_deaths, state_least_deaths_num_deaths, label = 'State With Least Number of Deaths', color = 'g') # Plots the information about the state with least number of Covid deaths
            plt.legend(shadow = True)                                                                                            # Adds a legend to the graph
            plt.ylabel('Number of Deaths')                                                                                       # Adds a label to the y-axis of the graph
            plt.xlabel('State')                                                                                                  # Adds a label to the x-axis of the graph
            plt.title('Comparison With Number of Deaths:')                                                                       # Adds a title to the graph
            plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)                                                  # Formats the ticks in the x-axis
            plt.show()                                                                                                           # Shows the graph to the user

        elif number_of_deaths == state_least_deaths_num_deaths:                                                                 # In case the state requested by the user is the state with least number of Covid deaths, a graph comparing the state requested by the user and the state with most number of Covid deaths is plotted
            
            print(state_requested, 'is the state with least number of deaths!')                                                 # Prints a message to the user informing that the state requested is the state with least number of Covid deaths
            plt.bar(state_most_cases, state_most_deaths_num_deaths, label = 'State With Most Number of Deaths', color = 'r')    # Plots the information about the state with most number of Covid deaths
            plt.bar(state_requested, number_of_deaths, label = 'State Requested', color = 'y')                                  # Plots the information about the state requested
            plt.legend(shadow = True)                                                                                           # Adds a legend to the graph
            plt.ylabel('Number of Deaths')                                                                                      # Adds a label to the y-axis of the graph
            plt.xlabel('State')                                                                                                 # Adds a label to the x-axis of the graph
            plt.title('Comparison With Number of Deaths:')                                                                      # Adds a title to the graph
            plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)                                                 # Formats the ticks in the x-axis
            plt.show()                                                                                                          # Shows the graph to the user

        else:
            plt.bar(state_most_deaths, state_most_deaths_num_deaths, label = 'State With Most Number of Deaths', color = 'r')    # Plots the information about the state with most number of Covid deaths
            plt.bar(state_requested, number_of_deaths, label = 'State Requested', color = 'y')                                   # Plots the information about the state requested
            plt.bar(state_least_deaths, state_least_deaths_num_deaths, label = 'State With Least Number of Deaths', color = 'g') # Plots the information about the state with least number of Covid deaths
            plt.legend(shadow = True)                                                                                            # Adds a legend to the graph
            plt.ylabel('Number of Deaths')                                                                                       # Adds a label to the y-axis of the graph
            plt.xlabel('State')                                                                                                  # Adds a label to the x-axis of the graph
            plt.title('Comparison With Number of Deaths:')                                                                       # Adds a title to the graph
            plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)                                                  # Formats the ticks in the x-axis
            plt.show()                                                                                                           # Shows the graph to the user


    if user_topic == 'B':                                                                                                       # If the user chose the topic 'B - Economics', the program presents the user with economic indicators from 2019 and 2020 of the state requested
        
        per_capita_2019 = float(array_per_capita[index_array_per_capita][2])                                                    # Gets the per capita personal income of 2019 from the state requested by the user
        per_capita_2020 = float(array_per_capita[index_array_per_capita][1])                                                    # Gets the per capita personal income of 2020 from the state requested by the user
        difference_per_capita_2019_2020 = per_capita_2020 - per_capita_2019                                                     # Calculates the difference between the per capita personal income of 2019 and 2020 of the state requested by the user

        if difference_per_capita_2019_2020 > 0:                                                                                                             # If the difference in the per capita personal income is positive, it means that the per capita personal income increased from 2019 to 2020
            print('The Per Capita Personal Income increased ${:.2f} from 2019 to 2020 in {}.'.format(difference_per_capita_2019_2020, state_requested))     # Prints a message to the user indicating how much in dolars did the per capita personal income increased from 2019 to 2020

        elif difference_per_capita_2019_2020 < 0:                                                                                                           # If the difference in the per capita personal income is negative, it means that the per capita personal income decreased from 2019 to 2020
            print('The Per Capita Personal Income decreased ${:.2f} from 2019 to 2020 in {}.'.format(difference_per_capita_2019_2020, state_requested))     # Prints a message to the user indicating how much in dolars did the per capita personal income decreased from 2019 to 2020

        elif difference_per_capita_2019_2020 == 0:                                                                                                          # If the difference in the per capita personal income is zero, it means that the per capita personal income continued the same from 2019 to 2020
            print('The Per Capita Personal Income continued the same from 2019 to 2020 in {}.'.format(state_requested))                                     # Prints a message to the user indicating that the per capita personal income remained the same from 2019 to 2020

        unemployment_rate_2019 = float(array_unemployment[index_array_unemployment][1])                                         # Gets the unemployment rate of 2019 of the state requested by the user
        unemployment_rate_2020 = float(array_unemployment[index_array_unemployment][2])                                         # Gets the unemployment rate of 2020 of the state requested by the user

        print('\nUnemployment Rate in 2019: {}'.format(unemployment_rate_2019))                                                 # Prints the unemployment rate in 2019 of the state requested by the user
        print('Unemployment Rate in 2020: {}'.format(unemployment_rate_2020))                                                   # Prints the unemployment rate in 2020 of the state requested by the user
        print('Change in Unemployment Rate from 2019 to 2020: {:.1f}'.format(unemployment_rate_2020-unemployment_rate_2019))    # Prints the difference in the unemployment rate from 2019 to 2020 in the state requested by the user

        unemployment_rates = [unemployment_rate_2019, unemployment_rate_2020]                                                   # Creates a list with the unemployment rates from 2019 and 2020 of the state requested by the user
        per_capitas = [per_capita_2019, per_capita_2020]                                                                        # Creates a list with the per capita personal income from 2019 and 2020 of the state requested by the user
        years = [2019, 2020]                                                                                                    # Creates a list with the years 2019 and 2020

        plt.subplot(2, 1, 1)                                                                                                    # Defines the subposition of the following plot                                                     
        plt.plot(years,per_capitas, linestyle = '--', color = 'deeppink', label = state_requested)                              # Plots the per capita personal incomes of 2019 and 2020 of the state requested by the user                  
        plt.legend(shadow = True)                                                                                               # Adds a legend to the graph
        plt.ylabel('Per Capita Personal Income in Dollars')                                                                     # Adds a label to the y-axis of the graph
        plt.ticklabel_format(useOffset=False)                                                                                   # Formats the ticks in the x-axis
        plt.xticks(years)                                                                                                       # Formats the ticks in the x-axis
        plt.title('Per Capita Personal Income:')                                                                                # Adds a title to the graph

        plt.subplot(2, 1, 2)                                                                                                    # Defines the subposition of the following plot                                                               
        plt.plot(years,unemployment_rates, linestyle = '--', color = 'navy', label = state_requested)                           # Plots the unemployment rates of 2019 and 2020 of the state requested by the user            
        plt.legend(shadow = True)                                                                                               # Adds a legend to the graph
        plt.ylabel('Unemployment Rate in %')                                                                                    # Adds a label to the y-axis of the graph
        plt.xlabel('Years')                                                                                                     # Adds a label to the x-axis of the graph
        plt.ticklabel_format(useOffset=False)                                                                                   # Formats the ticks in the x-axis
        plt.xticks(years)                                                                                                       # Formats the ticks in the x-axis
        plt.title('Unemployment Rate:')                                                                                         # Adds a title to the graph

        plt.show()                                                                                                              # Shows the graph to the user
                                              

if __name__ == '__main__':
    main()