# 1. Check whether a number is positive, negative, or zero.
a=int(input("Enter A number"))
if a>0:
    print("positive")
elif a<0:
    print("Negaative")
else:
    print("Zero")

# 2. Check whether a number is even or odd.
Num=int(input("Enter A Number"))
if Num %2==0:
    print("Even")
else:
    print("Odd")

# 3. Find the largest of two numbers.

Num1=int(input("Enter 1st Number"))
Num2=int(input("Enter 2nd Number"))
if Num1>Num2:
    print(Num1,"Is Greater")
else:
    print(Num2,"Is Smallest")

# 4. Find the largest of three numbers.
A=int(input("Enter first Number"))
B=int(input("Enter Second Number"))
C=int(input("Enter Third Number"))
if A>B and A>C:
    print(A)
elif B>A and B>C:
    print(B)
else:
    print(C)

# 5. Check whether a person is eligible to vote.
Person=int(input("Enter your Age"))
if Person>=18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

# 6. Check whether a year is a leap year.
Year=int(input("Enter Year"))
if Year%4==0 and Year%100!=0 or Year%400==0:
    print(Year,"Is The Leap Year ")
else:
    print(Year,"Is Not Leap Year")

# 7. Check whether a character is a vowel or consonant.
Character=input("Enter a Character")
if Character in 'aeiouAEIOU':
    print(Character,"Is Vowel")
else:
    print(Character,"is Consonant")

# 8. Check whether a character is an alphabet, digit, or special character.
Character=input("Enter The Character")
if 'A'<= Character>='Z' or 'a'<= Character >='z':
    print(Character,"Is Alphabet")
elif '0'< Character <= '9':
    print(Character,"Is Digit")
else:
    print(Character,"Is Special Character")

# 9. Create a simple calculator using if-elif.
Num1=float(input("Enter 1st Number"))
Operator=input("Enter Your Operator(+,-,*,/)")
Num2=float(input("Enter 2nd Number"))
if Operator=="+":
    print(Num1+Num2)
elif Operator=="-":
    print(Num1-Num2)
elif Operator=="*":
    print(Num1*Num2)
elif Operator=="/":
    print(Num1/Num2)
else:
    print("Invalid")

# 10. Check student grade based on marks.

Marks=float(input("Enter Your Marks"))
if Marks>=90:
    print("Grade A")
elif Marks>=80:
    print("Grade B")
elif Marks>=70:
    print("Grade C")
else:
    print("Grade D")

# 11. Print numbers from 1 to 10 using a loop.

for i in range(1,11):
    print(i)

# 12. Find the sum of numbers from 1 to n.
num=int(input("Enter A number"))
sum=0
i=1
while i<=num:

    sum=sum+i
    i=i+1
print("Sum of Digit is",sum)

# 13. Find factorial of a number.

Num=int(input("Enter A Number"))
fact=1
for i in range(1,Num+1):
    fact=fact*i
print("Factorial =",fact)

# 14. Print multiplication table of a number.

A=int(input("Enter A Number"))
for i in range(0,10):
    i+=1
    print(A*i)

# 15. Count the number of digits in a number.
A=int(input("Enter A Number"))
count=0
while A>0:
    count=count+1
    A=A//10
print("Count of the Number is",count)

# 16. Reverse a number using a loop.
num=int(input("Enter the Number"))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print("Reverse of the Number is",reverse)

# 17. Check whether a number is palindrome.
num=int(input("Enter the Number"))
reverse=0
original=num

while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if reverse==original:
    print("Palindrome")
else:
    print("Not Palindrome")

# 18. Find sum of digits of a number.
num=int(input("enter The Number"))
sum=0
while num>0:
    digit=num%10
    num=num//10
    sum=sum+digit
print("Sum of Digit is ",sum)

# 19. Print all even numbers from a list.
Number=[10,20,30,33,21,61,81,80]
print("Even Number are")
for i in Number:
    if i%2==0:
        print(i)

# 20. Find the largest element in a list without using max().
numbers = [25, 10, 45, 8, 67, 32,80]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest Element =", largest)


