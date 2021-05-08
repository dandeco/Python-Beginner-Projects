#The aim of this project is to build a basic calculator, that performs essential arithmetic functions of
#addition, subtraction, multiplication and division.

no_1 = float(input("Enter the first number: "))
operator = input("Enter the operator to be utilized: ")
no_2 = float(input("Enter in the second number: "))

if operator == "+" :
    print(no_1 + no_2)

elif operator == "-" :
    print(no_1 - no_2)

elif operator == "*" :
    print(no_1 * no_2)

elif operator == "/" :
    print(no_1 / no_2)

else:
    print("Invalid operator. Please select one of the following : + , - , * , / ")

