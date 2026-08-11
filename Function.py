#1
def hello():
    print("Hello Python")
hello()

#2
def Welcome():
    print("Welcome to Python Programming")
Welcome()

#3
def Show_Name():
    print("Abhishek")
Show_Name()

#4
def square():
    print(5*5)
square()

#5
def cube():
    print(3**3)
cube()

# 6
def greet(name):
    print("Hello",name)
greet("Abhishek")
greet("Saumya")

# 7
def add(a,b):
    print(a+b)
add(10,20)

# 8
def subtract(a,b):
    print(a-b)
subtract(20,10)

# 9
def multiply(a,b):
    print(a*b)
multiply(5,4)

# 10
def divide(a,b):
    print(a/b)
divide(20,5)

# 11
def square(n):
    return n*n
result=square(5)
print(result)

# 12
def cube(n):
    return n*n*n
result=cube(3)
print(result)

# 13
def add(a,b):
    return a+b
result=add(5,10)
print(result)

# 14
def average(a,b,c):
    return (a+b+c)/3
result=average(5,10,15)
print(result)

# 15
def area_of_rectangle(l,w):
    return(l*w)
result=area_of_rectangle(5,10)
print(result)

# 16
def even_odd(n):
    if n %2==0:
        return "Even"
    else:
        return"Odd"
result=even_odd(8)
print(result)

# 17
def check_positive(n):
    if n >0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "zero"
result=check_positive(5)
print(result)

# 18
def largest(a,b):
    if a>b:
        return "A is Greater"
    else:
        return "B is Greater"
result=largest(10,20)
print(result)

# 19
def largest(a,b,c):
    if a>b & b>c:
        return "A is Largest"
    elif b>c:
        return "B is Largest"
    else:
        return "C is Largest"

result=largest(100,40,30)
print(result)

# 20
def chek_pass(marks):
    if marks>=40:
        return "pass"
    else:
        return "Fail"

result=chek_pass(95)
print(result)
