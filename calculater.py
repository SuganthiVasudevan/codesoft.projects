print("Simple Calculater")

n1 = float(input("Enter number 1 : "))
n2 = float(input("Enter number 2 : "))

print("Choose operation")

operator = input("enter an operator (+ - * /):")

if operator == "+" :
    result = n1 + n2
    print(round(result,3))

elif operator == "-":
    result = n1 - n2
    print(round(result,3))

elif operator == "*":
    result = n1*n2
    print(round(result,3))

elif operator == "/":
    result = n1/n2
    print(round(result,3))

else: 
    print("Not Valid")

