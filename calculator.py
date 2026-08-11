a=int(input("enter the 1st Number"))
b=int(input("enter the 2nd Number"))

operator = input("Enter Operator(+,-,*,/) ")
if operator == "+":
    c = a + b
    print("Result",c)

elif operator == "-":
    c = a-b
    print("Result",c)

elif operator == "*":
    c=a*b
    print("Result",c)

elif operator == "/":
    c=a/b
    print("Result",c)
else:
    print("Incorrect Operator:")              

