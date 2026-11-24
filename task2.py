#1. Print Numbers 
for i in range(1,11):
    print(i)
#2. Print Even Numbers
for i in range(1,51):
    if i%2==0:
      print(i)
#3. Print Odd Numbers 
for i in range(1,101):
    if i%2!=0:
        print(i)
#4. Sum of Numbers 
sum=0
for i in range(1,101):
    sum=sum+i
print("Total Sum:",sum)
#5. Multiplication Table 
number=int(input("Enter a Number:"))
for i in range(1,11):
    print(number,"*",i,number*i)
#6. Reverse Counting 
for i in range(100,0,-1):
    print(i)
#7. Count Digits 
number=int(input("Enter Your Number:"))
count=0
while number>0:
    count=count+1
    number=number//10
print("Total Digits:",count)
#8. Factorial of a Number
number=int(input("Enter Your Number:"))
factorial=1
for i in range(1,number+1):
    factorial=factorial*i
print("Factorial",factorial)
#9. Reverse a Number
number=int(input("Enter your Number"))
reverse=0
while number>0:
    digit=number%10
    reverse=reverse*10+1
    number=number//10
print("Reverrsed Number:",reverse)
#10. Sum of Digits 
number=int(input("Enter Your Number:"))
total=0
while number>0:
    digit=number%10
    total=total+1
    number=number//10
print("Sum of Digit:", total)
#11. Palindrome Number
number=int(input("Enter Your Number:"))
original=number
reverse=0
while number>0:
    digit=number%10
    reverse=reverse*10+1
    number=number//10
if original==reverse:
    print("Its Palindrome")
else:
    print("Its Not Palindrome")
#12. Prime Number 
number=int(input("Enter Your Number:"))
count=0
for i in range(1,number+1):
    if number%i==0:
        count=count+1
if count==2:
    print("Prime number")
else:
    print("Its Not Prime Number")
#13. Fibonacci Series 
number=int(input("Enter Your  fibonacci Number:"))

x=0
y=1
for i in range(number):
    print(x,end="")
    z=x+y
    x=y
    y=z

#14. Find the Largest Number
largest=0
for i in range(5):
    number=int(input("Enter Largest Number:"))
    if number>largest:
        largest=number
print("Largest Number:",largest)
#15. Star Pattern
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

