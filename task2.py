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
