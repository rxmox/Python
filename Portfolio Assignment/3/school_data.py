# school_data.py
# Omar Ahmed, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

import numpy as np
import matplotlib.pyplot as plt

# The following class is provided and should not be modified.
class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))


# Import data here
data_2019 = np.genfromtxt('SchoolData_2018-2019.csv', delimiter = ',', skip_header = True)   #importing the arrays from the three csv files
data_2020 = np.genfromtxt('SchoolData_2019-2020.csv', delimiter = ',', skip_header = True)
data_2021 = np.genfromtxt('SchoolData_2020-2021.csv', delimiter = ',', skip_header = True)


# Hint: Create a dictionary for all school names and codes
schools_dict = {                                           #defining a dictionary containing all school names along with their codes
    '1224': 'Centennial High School',
    '1679': 'Robert Thirsk School',
    '9626': 'Louise Dean School',
    '9806': 'Queen Elizabeth High School',
    '9813': 'Forest Lawn High School',
    '9815': 'Crescent Heights High School',
    '9816': 'Western Canada High School',
    '9823': 'Central Memorial High School',
    '9825': 'James Fowler High School',
    '9826': 'Ernest Manning High School',
    '9829': 'William Aberhart High School',
    '9830': 'National Sport School',
    '9836': 'Henry Wise Wood High School',
    '9847': 'Bowness High School',
    '9850': 'Lord Beaverbrook High School',
    '9856': 'Jack James High School',
    '9857': 'Sir Winston Churchill High School',
    '9858': 'Dr. E. P. Scarlett High School',
    '9860': 'John G Diefenbaker High School',
    '9865': 'Lester B. Pearson High School'
}

# Hint: Create a list of school codes to help with index look-up in arrays
schools_codes = list(schools_dict.keys())                                  #placing all the school codes from the dictionary in a list

#Add your code within the main function. A docstring is not required for this function.
def main():
    print("ENDG 233 School Enrollment Statistics\n")                       #header of program

    # Print array data here
    print(f'Array data for 2020 - 2021:\n {data_2021}')                    #displaying the arrays from the three csv files
    print(f'Array data for 2019 - 2020:\n {data_2020}')
    print(f'Array data for 2018 - 2019:\n {data_2019}')


    # Add request for user input here
    while True:                                                         #continuous input loop checking validity of user input
        school_input = input('Please enter the high school name or school code: ')
        if school_input in schools_codes or school_input in schools_dict.values():                 
            break
        else:
            print('You must enter a valid school name or code')
    
    print("\n***Requested School Statistics***\n")

    # Print school name and code using the given class
    if school_input.isnumeric() is True:                 #checking wether user entered school name or code
        name = schools_dict.get(school_input)                 
        code = (school_input)
    else:
        name = school_input  
        for key, value in schools_dict.items():
            if school_input == value:
                code = key                             

    school_info= School(name, code)                     
    school_info.print_all_stats()                        #displaying school info

    #Add data processing and plotting here  
    position = schools_codes.index(code)        #getting the index of entered school
    mean_grade_10 = int((data_2019[position][1] + data_2020[position][1] + data_2021[position][1])/3) #calculating the mean for each grade
    mean_grade_11 = int((data_2019[position][2] + data_2020[position][2] + data_2021[position][2])/3)
    mean_grade_12 = int((data_2019[position][3] + data_2020[position][3] + data_2021[position][3])/3)
    grad_students = int(mean_grade_12 * 3)     #calculating the number of students that graduated

    print(f'Mean enrollment for Grade 10:  {mean_grade_10}')             #displaying the mean for each grade
    print(f'Mean enrollment for Grade 11:  {mean_grade_11}')
    print(f'Mean enrollment for Grade 12:  {mean_grade_12}')
    print(f'Total number of students who graduated in the past three years: {grad_students}')#displaying the number of students that graduated

    years = np.array(range(2019, 2022))      #creates an array for years
    grades = np.array(range(10, 13))         #creates an array for grades

    plt.plot(grades, data_2021[position][1:], 'bo', label = '2021 Enrollment') #plotting 2021 data using blue points
    plt.plot(grades, data_2020[position][1:], 'go', label = '2020 Enrollment') #plotting 2020 data using green points
    plt.plot(grades, data_2019[position][1:], 'ro', label = '2019 Enrollment') #plotting 2019 data using red points
    
    plt.xlabel("Grade Level")                #gives x-axis label
    plt.ylabel("Number of Students")         #gives y-axis label
    plt.xticks(grades)                       #sets ticks for x-axis
    plt.title('Grade Enrollment by Year')    #gives title to graph
    plt.legend()                             #giving the graph a legend

    plt.show()                               #displaying the graph

    #BONUS
    grade_10 = [(data_2019[position][1]), (data_2020[position][1]), (data_2021[position][1])] #creating an array for grade 10 data from all years
    grade_11 = [(data_2019[position][2]), (data_2020[position][2]), (data_2021[position][2])] #creating an array for grade 11 data from all years
    grade_12 = [(data_2019[position][3]), (data_2020[position][3]), (data_2021[position][3])] #creating an array for grade 12 data from all years

    plt.subplot(3,1,1)                                    #creating first subplot
    plt.plot(years, grade_10, 'y--', label = 'Grade 10')  #plots data for grade 10         
    plt.xlabel("Enrollment Year")                         #gives x-axis label
    plt.ylabel("Number of students")                      #gives y-axis label
    plt.xticks(years)                                     #sets ticks for x-axis
    plt.title('Enrollment by Grade')                      #gives title to graph
    plt.legend()                                          #giving the graph a legend

    plt.subplot(3,1,2)                                    #creating second subplot
    plt.plot(years, grade_11, 'm--', label = 'Grade 11')  #plots data for grade 11            
    plt.xlabel("Enrollment Year")                         #gives x-axis label
    plt.ylabel("Number of students")                      #gives y-axis label
    plt.xticks(years)                                     #sets ticks for x-axis
    plt.legend()                                          #giving the graph a legend

    plt.subplot(3,1,3)                                    #creating third subplot
    plt.plot(years, grade_12, 'c--', label = 'Grade 12')  #plots data for grade 11             
    plt.xlabel("Enrollment Year")                         #gives x-axis label
    plt.ylabel("Number of students")                      #gives y-axis label
    plt.xticks(years)                                     #sets ticks for x-axis
    plt.legend()                                          #giving the graph a legend

    plt.show()                                            #displaying the graph

# Do not modify the code below
if __name__ == '__main__':
    main()
