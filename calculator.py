#this is a calculator project
number1 = eval(input("enter_first_number:"))
number2= eval(input("enter_second_number:"))
operator = input("enter_operator:")
def add(num1,num2):
    result = num1 + num2
    print(result)



def subtract(num1,num2):
    result = num1 - num2
    print(result)

def divide(num1,num2):
    result = num1/num2
    print(result)

def multiply(num1,num2):
    result = num1*num2
    print(result)

#check on operator
if operator == "+":
    add(number1,number2)
elif operator == "-":
    subtract(number1,number2)
elif operator =="/":
    divide(number1,number2)
elif operator == "X" or operator == "X" or operator == "*":
    multiply(number1,number2)
else:
    print("invalid operator")
