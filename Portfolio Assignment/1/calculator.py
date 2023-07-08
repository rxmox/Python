# calculator.py
# Omar Ahmed, ENDG 233 F21
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.
#
num_1= int(input('Enter the first number: '))       #Asking the user to input 3 numbers and 2 operators, and assigning them to variables
op_1= input('for addition type +, for subtraction type -, for multiplication type *, for division type /: ')   
num_2= int(input('Enter the second number: '))                                                                 
op_2= input('for addition type +, for subtraction type -, for multiplication type *, for division type /: ')  
num_3= int(input('Enter the third number: '))                                                                  

print(f'The original expression is: {num_1} {op_1} {num_2} {op_2} {num_3}')  #Displaying the values entered by the user in order

if op_1 == '/' and op_2 == '/':     #if and elif statements for all 16 combinations of numbers and operators
    total= num_1//num_2//num_3      #the operators are compared and a different calculation is made depending on the operators entered
elif op_1 == '/' and op_2 == '*':
    total= num_1//num_2*num_3
elif op_1 == '/' and op_2 == '+':
    total= num_1//num_2+num_3
elif op_1 == '/' and op_2 == '-':
    total= num_1//num_2-num_3

if op_1 == '*' and op_2 == '/':
    total= num_1*num_2//num_3
elif op_1 == '*' and op_2 == '*':
    total= num_1*num_2*num_3
elif op_1 == '*' and op_2 == '+':
    total= num_1*num_2+num_3
elif op_1 == '*' and op_2 == '-':
    total= num_1*num_2-num_3

if op_1 == '+' and op_2 == '/':
    total= num_1+num_2//num_3
elif op_1 == '+' and op_2 == '*':
    total= num_1+num_2*num_3
elif op_1 == '+' and op_2 == '+':
    total= num_1+num_2+num_3
elif op_1 == '+' and op_2 == '-':
    total= num_1+num_2-num_3

if op_1 == '-' and op_2 == '/':
    total= num_1-num_2//num_3
elif op_1 == '-' and op_2 == '*':
    total= num_1-num_2*num_3
elif op_1 == '-' and op_2 == '+':
    total= num_1-num_2+num_3
elif op_1 == '-' and op_2 == '-':
    total= num_1-num_2-num_3

print(total)              #Displaying to the user the total value of the combination of numbers and operators entered