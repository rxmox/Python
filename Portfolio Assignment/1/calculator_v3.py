#Receiving integers and operators from the user
intro = ("Enter an expression consisting of 3 integers and\n"
        "2 operators (+,-,/,*), make sure to enter a space\n"
        "between each integer/expression\n"
        "\nExpression: ")
int_1, op_1, int_2, op_2, int_3 = input(intro).split()
integers = [int(int_1), int(int_2), int(int_3)]
operators = [op_1, op_2]

#Receiving the result from an operation
def handling_operations(int1, int2, operator):
    operations = {
        '+': int1 + int2,
        '-': int1 - int2,
        '/': int1 // int2,
        '*': int1 * int2
    }
    return operations[operator]

#Displaying the full experssion to the user
def displaying_result(integers, operators, result):
    for i in range(0,3):
        print(str(integers[i]), end = " ")
        if i != 2:
            print(str(operators[i]), end = " ")
    print("= ",result)

#Handling BODMAS
if operators[1] == '*' or operators[1] == '/':
    result = handling_operations(integers[0], handling_operations(integers[1], integers[2], operators[1]), operators[0])
else:
    result = handling_operations(handling_operations(integers[0], integers[1], operators[0]), integers[2] , operators[1])

#Displaying the result
print("The original expression is:", end = " ")
displaying_result(integers, operators, result)