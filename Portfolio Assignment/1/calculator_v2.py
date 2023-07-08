#This code does not follow bodmas
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
}

integers = []
operators = []
for i in range(0,3):
    integer = int(input("Enter an integer: "))
    integers.append(integer)
    if i != 2:
        operator_ = input("Enter an operator: ")
        operators.append(operator_)



if operators[1] == '*' or operators[0] == '/':
    x = ops[operators[1]](integers[1],integers[2])
    result = ops[operators[0]](integers[0],x)
else:
    x = ops[operators[0]](integers[0],integers[1])
    result = ops[operators[1]](x,integers[2])

print(result)