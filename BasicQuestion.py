#1. Print the message: Hello, World!
print("Hello, World!")


#Create a variable name and store your name. Print it.

name="Abhishek"
print(name)

#Create two variables a = 10 and b = 20. Print their sum.

a=10
b=20
print(a+b)

#4. Store your age in a variable and print: My age is 23

age=21
print("My Age is",age)

#Swap two variables without using a third variable.

a=10
b=15
c=a #10
a=b #15
b=c #10


print(a)
print(b)
print(c)

#Swap two variables without using a third variable.

a=10
b=20
a = a+b #30
b= a%b #10
a = a-b #10
print(a)
print(b)

#Swap two variables without using a third variable.

a=10
b=20
a,b=b,a
print(a)
print(b)

a=10
b=20
print(a-b)

# Level 2: User Input (6-10)
#6. Take a user's name as input and print:Welcome, Vijaya!

name=input("Enter Your Name\n")
print("Welcome",name)

# 7. Take two numbers as input and print:Addition
a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))
c=a+b
print("The Sum of Two Number is ",c)

# 7. Take two numbers as input and print:Subtraction
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
c=a-b

print(c)
# 7. Take two numbers as input and print:Multiplication
a=int(input("Enter 1st Number\n"))
b=int(input("Enter 2nd Number\n"))
c=a*b
print(c)

# 7. Take two numbers as input and print:Division
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
c=a/b
print(c)

#Take the radius of a circle as input and find its area.
radius=int(input("Enter the Radius of The Circle"))

area = 3.14* radius ** 2
print(area)

#Take a temperature in Celsius and convert it to Fahrenheit.
celcius=float(input("Enter your Temperature In Celcius"))

fahrenheit= celcius * 1.8 +32

print(fahrenheit)

#Take a number and print whether it is even or odd.
a=int(input("Enter a Number"))
if a % 2 ==0:
    print("Even")
else:
    print("Odd")

#11. Take a number and check whether it is positive, negative, or zero.
a=float(input("Enter a Number"))
if a > 0:
    print("Positive")
elif a< 0:
    print("Negative")
else:
    print("Zero")

#12. Take a person's age and check whether they are eligible to vote.
age=int(input("Enter Your Age"))
if age>=18:
    print("You are Eligible to Vote")
else:
    print("You Are Not Eligible To Vote")

#Take three numbers and print the largest one.
a=int(input("Enter The First Number"))
b=int(input("Enter The Second Number"))
c=int(input("Enter The Third Number"))

if a > b and a>c:
    print("A is Greatest")
elif b>a and b>c:
    print("B is Greatest")
else:
    print("C is Greatest")

#14. Take marks as input and print:14.
# 90–100 → A
#80–89 → B
#70–79 → C
#Below 70 → Fail

Marks=int(input("Enter Your Marks"))
if Marks >=90:
    print("You Secured Grade A")
elif Marks >=80:
    print("You Have Secured Grade B")
elif Marks >=70:
    print("You Have Secured Grade C")
else:
    print("You Are Fail")

#Check whether a year is a leap year.
Year=int(input("Enter The year "))
if Year %4 ==0 and Year%100 !=0 or Year%400==0:
    print("This",Year,"Is Leap Year")
else:
    print("This",Year,"Is Not Leap Year")

#Level 4: Loops (16-20)

#16. Print numbers from 1 to 10 using a for loop.
i=1
while i<=10:
    print(i)
    i+=1

#16. Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

#17. Print the multiplication table of a given number.
a=5
for i in range(1,11):
    print(a ,"X",i, "=",a*i)

#Find the sum of numbers from 1 to 100.
total=0
for i in range(1,101):
    total=total+i
    print(total)

#19. Count how many vowels are present in a given string.
string=(input("Enter A String"))
count=0
for char in string:
    if char in"aeiouAEIOU":
        count +=1
print("Number of vowel is",count)

#Reverse a string without using slicing ([::-1]).

string=input("Enter A String")
reverse=""

for char in string:
    reverse=char+reverse
print(reverse)

#1. Check Positive Number , Take a number as input.if the number is positive, print "Positive".

Number=int(input("Enter A Number"))
if Number >0:
    print("Positive")
else:
    print("Invalid")

#2. Check Negative Number,Take a number as input. If the number is negative, print "Negative".
Number=int(input("Enter A Number"))
if Number <0:
    print("Negative")
else:
    print("Invalid")

#3. Check Zero,Take a number as input,If the number is zero, print "Zero".
Number=int(input("Enter A Number"))
if Number==0:
    print("Zero")
else:
    print("Invalid")

#4. Even or Odd,Take a number as input.,Print whether it is even or odd.

a=int(input("Enter A Number"))
if a%2==0:
    print("Even Number")
else:
    print("Odd Number")

#5. Divisible by 5,Take a number as input.Print whether it is divisible by 5.

Number=int(input("Enter A Number"))
if Number %5==0:
    print("Divisible By 5")
else:
    print("Not Divisible By 5")

#6. Positive, Negative, or Zero,Take a number as input.Print whether it is positive, negative, or zero.

Number=int(input("Enter A number"))
if Number >0:
    print("Positive Number")
elif Number <0:
    print("Negative Number")
else:
    print("Zero")

#7. Eligible to Vote
Age=int(input("Enter Your Age"))
if Age >= 18:
    print("You Are Eligible to Vote")
else:
    print("Not Eligible to Vote")

#8. Pass or Fail,Take marks as input. Marks ≥ 40 → Pass,Otherwise → Fail
Marks=float(input("Enter Your Marks"))
if Marks >= 40:
    print("You Are Pass")
else:
    print("You Are Fail")

#9. Greatest of Two Numbers

A=int(input("Enter First Number"))
B=int(input("Enter Second Number"))

if A>B:
    print("A is Greater")
else:
    print("B is Greater")

#10. Smallest of Two Numbers

A=int(input("Enter First Number"))
B=int(input("Enter Second Number"))
if A<B:
    print("A is Smallest")
else:
    print("B is Smallest")

#11. Greatest of Three Numbers
A=int(input("Enter First Number"))
B=int(input("Enter Second Number"))
C=int(input("Enter Third Number"))

if A>B and A>C:
    print("A is Largest")
elif B>A and B>C:
    print("B is Greatest")
else:
    print("C is Greatest")

#12. Smallest of Three Numbers
A=int(input("Enter First Number"))
B=int(input("Enter Second Number"))
C=int(input("Enter Third Number"))

if A<B & A<C:
    print("A is Smallest")
elif B<A and B<C:
    print("B is Smallest")
else:
    print("C is Smallest")

#13. Leap Year
year=int(input("Enter Year"))
if year%4==0 & year%100!=0 or year%400==0:
    print("This",year,"Is Leap Year")
else:
    print("This",year,"Is Not Leap Year")

#14. Vowel or Consonant
Alphabet=input("Enter A Alphabet")
if Alphabet in "aeiouAEIOU":
    print("Vowel")
else:
    print("Constant")

#15. Grade Calculator
# Take marks and print:
# 90–100 → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# Below 60 → Fail

Marks=int(input("Enter Your Marks"))
if Marks >=90:
    print("You Have Secured Grade A")
elif Marks >=80:
    print("You Have Secured Grade B")
elif Marks >=70:
    print("You have Secured Grade C")
elif Marks >=60:
    print("You Have Secured Grade D")
else:
    print("You Are Fail")

#16. Check Number Range
# Take a number.
# Print whether it lies between 1 and 100.

A=int(input("Enter A Number"))
if A in range(1,101):
    print("Exist")
else:
    print("not Exist")

#16. Check Number Range
# Take a number.
# Print whether it lies between 1 and 100.
A=int(input("Enter A Number"))
if 1<= A <=100:
    print("Number is Exist B/W 1-100")
else:
    print("NUmber is Not Exist")

# 17. Divisible by 3 and 5
# Take a number.
# Check whether it is divisible by both 3 and 5.

A=int(input("Enter A Number"))
if A%3==0 & A%5==0:
    print("Number is Divisible by Both 3 And 5")
else:
    print("Number is Not Divisible bye Both 3 And 5")

#18. Simple Calculator

Number1=float(input("Enter First Number"))
Operator=input("Enter Operator(+,-,*,/)")
Number2=float(input("Enter Second Number"))

if Operator =="+":
    print(Number1+Number2)
elif Operator =="-":
    print(Number1-Number2)
elif Operator =="*":
    print(Number1*Number2)
elif Operator =="/":
    if Number2!=0:
        print(Number1/Number2)
    else:
        print("Cannot Divide By Zero")
else:
    print("Invalid Operator")

#Take Input string and Find The Duplicate Value and Ocuurance

String=input("Enter the string")
for char in String:
    count=0
    for ch in String:
        if char==ch:
            count +=1

    if count > 1:
        print(char,count)

#Take String From User And Find The Duplicate And Occurance Of String
String=input("Enter the String")
for Char in String:
    count=0
    for ch in String:
        if Char==ch:
            count +=1
    if count > 1:
        print(Char ,":", count)
# 19. ATM Withdrawal
# Take:Account balance
# Withdrawal amount
# Print:Transaction Successful if balance is sufficient.,Insufficient Balance otherwise.

print("Hello Costumer")

Amount=int(input("Enter Your Balance"))
Withdrawl=int(input("Enter your Withdrawl Amount"))
if Amount >= Withdrawl:
    print("Transaction Successfull")
else:
    print("Insufficient balance")

# 20. Login System
# Create:
# username = "admin"
# password = "1234"
# Take username and password as input.python BasicQuestion.py
# If both are correct → Login Successful
# Otherwise → Invalid Username or Password

username="admin"
password="1234"

A=input("Enter Your User Name")
B=(input("Enter Your Password"))
if A==username and B==password:
    print("Login Successfully")
else:
    print("Invalid User Name Or Password")




