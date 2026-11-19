
#1.Positive or Negative: Write a Python program to check whether a number is positive or negative.
a=int(input("Enter Your Number"))
if a>0:
    print("Positive Number:")
elif a<0:
    print("Negative Number:")
else:
    print("zero")
#2.Even or Odd: Write a program to check whether a given number is even or odd.
b=int(input("Enter your Number:"))
if b%2==0:
    print("even")
else:
    print("odd")

#3.Voting Eligibility: Ask the user for their age. Check whether they are eligible to vote (18 or above)
age=18
if age >=16:
    print("Eligible For Vote")
else:
    print("Not Eligible for Vote")

#4.Greater Number: Get two numbers from the user and print the greater number.
a=int(input("Enter Your First Number:"))
b=int(input("Enter Your Second Number"))
if a>=b:
    print("Greater Number")
else:
    print("Not Greater Number")

#5.Pass or Fail: Ask the user to enter their mark. If the mark is 35 or above, print "Pass"; otherwise, print "Fail".
marks=int(input("Enter Your Marks:"))
if marks>=35:
    print("Pass")
else:
    print("Fail")
#6.Zero or Non-Zero: Write a program to check whether a number is zero or non-zero.
number=int(input("enter Your Number:"))
if number==0:
    print("Zero")
else:
    print("Non Zero")
#7.Divisible by 5: Check whether a given number is divisible by 5.
a=(int(input("Enter Your Number")))
if a%5==0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")
#8.Temperature Check: Ask the user for the temperature. If it is above 30, print "Hot"; otherwise, print "Normal".
Temp=int(input("Enter Your Temprature:"))
if Temp >=30:
    print("Hot")
else:
    print("Normal")

#9.Password Check: Ask the user to enter a password. If it matches "python123", print "Login Successful"; otherwise, print "Wrong Password".
pwd=int(input("Enter Your Password:"))
if pwd =="Python123":
    print("Login Sucessfull")
else:
    print("Wrong Password")
#10.Smallest Number: Get two numbers and print the smaller number.
a=int(input("Enter Your First Number:"))
b=int(input("Enter Your Second Number"))
if a<=b:
    print("Smaller Number")
else:
    print("Not Smaller Number")
#part 2
#11.Positive, Negative or Zero: Check whether a number is positive, negative, or zero.
number=(int(input("Enter Your Number:")))
if number>=0:
    print("Positive")
elif number<=0:
    print("Negative")
else:
    print("Zero")
#12.Grade Calculator: Get a student's mark and display:
#◦ 90–100: Grade A
#◦	80–89: Grade B
#◦	70–79: Grade C
#◦	60–69: Grade D
#◦	Below 60: Fail
marks=int(input("Enter Your Number:"))
if marks >=90:
    print("Grade A")
elif marks >=89:
    print("Grade B")
elif marks >=70:
    print("Grade C")
elif marks >=60:
    print("Grade D")
else:
    print("Fail")

#13.	Age Category: Ask for age and display:
#	◦	0–12: Child
#	◦	13–19: Teenager
#	◦	20–59: Adult
#   ◦	60 and above: Senior Citizen
age=int(input("Enter Your Age:"))
if age<=12:
    print("Child")
elif age<=19:
    print("Teenager")
elif age<=59:
    print("Adult")
else:
    print("Senior Citizen")
#14.Largest of Three Numbers: Get three numbers and find the largest number.
a=int(input("Enter Your  First Number:"))
b=int(input("Enter your second Number:"))
c=int(input("Enter Your  Third NUmber:"))
if a>=b and a>=c:
    print("A is Largest Number")
elif b>=a and b>=c:
    print("B is Largest Number")
else:
    print("C is Largest")
#15.Day Number: Ask the user to enter a number from 1 to 7 and display the corresponding day of the week.
day=int(input("Enter Your Number:"))
if day==1:
    print("Sunday")
elif day==2:
    print("Monday")
elif day==3:
    print("Tuesday")
elif day==4:
    print("Wednesday")
elif day==5:
    print("Thursday")
elif day==6:
    print("Friday")
elif day==7:
    print("Saturday")
else:
    print("Invalid Number")
#16.Month Number: Ask the user to enter a number from 1 to 12 and display the month name.
months=int(input("Enter The Month Num:"))
if months==1:
    print("January")
elif months==2:
    print("Febrauary")
elif months==3:
    print("March")
elif months==4:
    print("April")
elif months==5:
    print("May")
elif months==6:
    print("June")
elif months==7:
    print("July")
elif months==8:
    print("Augest")
elif months==9:
    print("September")
elif months==10:
    print("October")
elif months==11:
    print("November")
elif months==12:
    print("December")
else:
    print("Invalid Month Number")

#17.Electricity Bill: Calculate the electricity bill based on units consumed:
#◦	Up to 100 units: ₹2 per unit
#◦	101–200 units: ₹3 per unit
#◦	Above 200 units: ₹5 per unit
units=int(input("Enter The Units Consumed"))
if units<=100:
    bill=units*2
elif units<=200:
    bill=units*3
else:
    bill=units*5
print("Electricity bill",bill)
#18.Simple Calculator: Ask the user for two numbers and an operator (+, -, *, /). Perform the selected operation.
a=float(input("Enter Your first Number:"))
b=float(input("Enter Your Second Number:"))
operators=input("Enter The Operator:")
if operators=="+":
    print(a+b)
elif operators=="-":
    print(a-b)
elif operators=="*":
    print(a*b)
elif operators=="/":
    if b!=0:
        print(a/b)
    else:
        print("Cannot divided by zero")
else:
    print("Invalid operator")
#19.Vowel or Consonant: Ask the user to enter an alphabet and check whether it is a vowel or consonant.
character=input("Enter the Alphabet:")
if character=="a":
    print("vowel")
elif character=="e":
    print("vowel") 
elif character=="i":
    print("vowel")
elif character=="o":
    print("vowel")
elif character=="u":
    print("vowel")
else:
    print("Consonant")
#20.Triangle Type: Get three sides of a triangle and identify whether it is:
#	◦	Equilateral
#	◦	Isosceles
#   ◦	Scalene
a=int(input("Enter the First Side:"))
b=int(input("Enter the Second  Side:"))
c=int(input("Enter the Third Side:"))
if a==b and b==c:
    print("Equilateral")
elif a==b or b==a or c==a:
    print("Isoscales")
else:
    print("Scalene")
#part3
#21.Leap Year: Write a program to check whether a given year is a leap year.
year=input("Enter the Year:")
if year%4==0:
    print("Leap Year")
else:
    print("Not Leap Year")
#22.Shopping Discount: Ask the user for the shopping amount:
#	◦	Above ₹5000: 20% discount
#	◦	Above ₹3000: 10% discount
#	◦	Otherwise: No discount 
amount=float(input("Enter The Amount:"))
if amount>=5000:
    print("20% Discount")
    print(final_amount=amount-amount*20/100)
elif amount>=3000:
    print("10% Discount")
    print(final_amount=amount-amount*20/100)
else:
    print("No Discount")
    print("Final_Amount", amount)

#23.ATM Withdrawal: Ask the user for their account balance and withdrawal amount. Check whether they have sufficient balance
balance=float(input("Enter the Account Balance:"))
Withdrawal=float(input("Enter the Withdrawal Amount:"))
if Withdrawal<=balance:
    print("Sufficiant Balance")
else:
    print("InSufficiant Balance")
#24.Login System: Ask for a username and password. Check whether both match the stored username and password.
username=input("Enter the Username:")
password=input("Enter the Password")
if username=="admin" and password=="Python123":
    print("Login Successfull")
else:
    print("Login  Not Successfull")
#25.	BMI Calculator: Ask for weight in kilograms and height in metres. Calculate BMI and display:
#	◦	Below 18.5: Underweight
#	◦	18.5–24.9: Normal
#	◦	25–29.9: Overweight
#	◦	30 or above: Obese
weight=float(input("Enter the weight:"))
height=float(input("Enter the height"))
bmi=weight/height*height
if bmi<=18.5:
    print("Underweight")
elif bmi<=24.9:
    print("Normal")
elif bmi<=29.9:
    print("overweight")
else:
    print("obese")
print("BMI Calculate",bmi)
#26.	Ticket Price: Ask for the age of a passenger:
#	◦	Below 5: Free
#   ◦	5–17: ₹50
#	◦	18–59: ₹100
#	◦	60 and above: ₹60#
age=int(input("Enter the Passanger Age:"))
if age<=5:
    print("Ticket Price: free")
elif age<=17:
    print("Ticket Price: 50rs")
elif age<=59:
    print("Ticket Price: 100rs")
else:
    print("Ticket Price: 100rs")
#27.	Number Range: Ask the user for a number and check whether it belongs to:
#	◦	1–50
#	◦	51–100
#	◦	Above 100
#	◦	Zero or negative
number=int(input("Enter the Number:"))
if number<=0:
    print("Zero or Negative")
elif number<=50:
    print("range 1-50")
elif number<=100:
    print("range 51-100")
else:
    print("Above 100")
#28.	Character Checker: Ask the user to enter one character and identify whether it is an uppercase letter, lowercase letter, digit, or special character.
char=input("Enter the Character:")
if char>='A' and char<='Z':
    print("UpperCase letter")
elif char>='a' and char<='b':
    print("Lowercase letter")
elif char>='0' and char<='9':
    print("digit")
else:
    print("Special Character")
#29.	Water Level Alert: Ask the user for the water tank level percentage:
#	◦	Below 20%: Low Level
#	◦	20–80%: Normal Level
#	◦	Above 80%: High Level
#	◦	100%: Tank Full
level=int(input("Enter the Tank Percentage Level:"))
if level ==100:
    print("Tank full")
elif level<=20:
    print("low level")
elif level<=80:
    print("Normal level")
else:
    print("High level")
#30.Mini Quiz: Ask the user a multiple-choice question. Check the answer and display "Correct Answer" or "Wrong Answer".
print("What is your Fav Color?")
print("A.Red")
print("B.Blue")
print("C.Yellow")
answer=input("Enter Your Answer:")
if answer=="A":
    print("Correct Answer")
else:
    print("Wrong Answer")
    