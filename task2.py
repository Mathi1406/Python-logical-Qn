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
  