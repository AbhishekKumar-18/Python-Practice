#Q1. Even or Odd
a=int(input("Enter A number"))
if a%2==0:
    print("Even")
else:
    print("Odd")

# Q2.Greater of Two Numbers

A=int(input("Enter 1st Number"))
B=int(input("Enter 2nd Number"))
if A>B:
    print("A is Greater")
else:
    print("B is Greater")

# Q3.Largest of Three Numbers
A=int(input("Enter 1st Number"))
B=int(input("Enter 2nd Number"))
C=int(input("Enter 3rd Number"))

if A>B and A>C:
    print("A is Greater")
elif B>A and B>C:
    print("B is Greater")
else:
    print("C is Greater")

# Q4.Positive, Negative, or Zero

A=int(input("Enter A Number"))
if A>0:
    print("Positive")
elif A<0:
    print("Negative")
else:
    print("Zero")

# Q5.Leap Year Check

year=int(input("Enter Year"))
if year%4==0 & year%100!=0 or year%400==0:
    print("The",year,"is Leap Year")
else:
    print("The",year,"is Not Leap Year")

#Q6.Print 1–100

for i in range(0,100):
    i+=1
    print(i)
#Q7.Print Even Numbers (1–100)
for i in range(0,100):
    i+=1
    if i %2==0:
        print(i,"Even")

#Q8.Multiplication Table
A=6
for i in range (0,10):
    i+=1
    print(A*i)


#Q8.Multiplication Table
A=6
for i in range (0,10):
    i+=1
    print(A,"X",i,"=",A*i)

#Q9.Sum of First N Natural Numbers

a=int(input("Enter A Number"))
sum= a*(a+1)//2
print("The Sum is",sum)

#Q10.Factorial of a Number
A=int(input("Enter the Number"))
B=1
for i in range(1,A+1):
    B=B*i
print("The Factorial is",B)

#Q11.Reverse a Number

num=int(input("Enter A Number"))
reverse=0

while num>0:
    digit =num%10
    reverse=reverse *10 + digit
    num=num//10

print("Reverse Of number is", reverse)

#Q12.Count Digits
num=int(input("Enter A Number"))
count = 0
while num>0:
    count = count+1
    num= num//10
print("Count of Number is",count)

#Q13.Sum of Digits

num=int(input("Enter A number"))
sum=0
while num>0:
    digit=num%10
    num=num//10
    sum=sum+digit
print("Sum of Digit is",sum)

#Q14.Palindrome Number

num=int(input("Enter A Number"))
reverse=0
original=num
while num>0:
    digit =num%10
    reverse=reverse *10 + digit
    num=num//10
if reverse==original:
    print("Palindrome")
else:
    print("Not Palindrome")

#Q15.Armstrong Number

num=int(input("Enter A number"))
sum=0
original = num
while num>0:
    digit=num%10
    sum= sum + digit **3
    num=num//10
if sum==original:
    print("is Armstrong")
else:
    print("is Not Armstrong")

# Loops & Patterns (16–25)

#Q16.Star Pattern (Increasing)

r=int(input("enter A number"))
for i in range(1,r+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#Q17.Star Pattern (Decreasing)

n=int(input("Enter A Number"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#Q18.Number Pattern (12345)

r=int(input("enter A number"))
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#Q19.Reverse Number Pattern (54321)

n=int(input("enter A Number"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

#Q20.Find Factors of a Number

num=int(input("Enter A Number"))
print("Factor of Number are")

for i in range(1,num+1):
    if num%i==0:
        print(i)

#Q21.Prime Number Check

num=int(input("Enter A number"))
count = 0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count ==2:
    print(num,"is Prime")
else:
    print(num,"is Not Prime")

#Q22.Print Prime Numbers (1–100)

for num in range(1,101):
    count =0
    for i in range(1,num+1):
        if num % i==0:
            count=count+1
    if count==2:
        print(num)
#Q23.Find GCD
A=int(input("Enter First Number"))
B=int(input("Enter Second Number"))
gcd=1
for i in range(1,min(A,B)+1):
    if A %i==0 and B %i==0:
        gcd=i
print("GCD=",gcd)

#Q24.Find LCM
A=int(input("Enter the First number"))
B=int(input("enter the Second number"))

for i in range(max(A,B),(A*B)+1):
    if i % A==0 and i % B==0:
        print("LCM =",i)
        break

#Q25.Fibonacci Series

n=int(input("Enter A Number"))
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c
