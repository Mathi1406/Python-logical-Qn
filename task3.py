#1. Create a dictionary for a student with the keys name, age, course, and mark. Add suitable values and print each key-value pair.
student={
    "name":"Mathisri"
    "age":25
    "course":"Python"
    "mark":
}
for key ,value in student.items():
    print(key,":",value)

#Create a dictionary containing five products and their prices. Ask the user to enter a product name and display its price. If the product does not exist, display a suitable message.
products={
    "Laptop":45000,"Mouse":500,"Keyboard":1000,"Monitor":12000,"Headphone":1500
}
product=input("Enter Your Product Name")
price=products.get(product)
if price is not None:
    print("Product Price:",price)
else:
    ("Product Not Found")
    
#3. Given a dictionary of student marks, add a new student, update the marks of an existing student, and print the updated dictionary.
student={
    "Arun":80,
    "kumar":75,
    ""Ravi":90
}
students["Bala"]=85
students.update[{"kumar:95"}]
print(students)
#Write a program that counts the frequency of each character in the string "python programming" using a dictionary.
text="python programming"
frequency={}
for char in text:
    if char in frequency:
        frequency[char]+1
    else:
        frequency[char]=1
print(frequency)
#Write a program that counts how many times each word appears in a sentence. Ignore differences between uppercase and lowercase letters.
sentence="Python is easy and python is powerful"
sentence=sentence.lower()
words=sentence.split()
frequency={}
for word in words:
    if word in frequency:
        frequency[word]+1
    else:
        frequency[word]=1
print(frequency)
#Create a dictionary of five employees and their salaries. Print only the employees whose salary is greater than 30000.
employees={
    "Mathi":25000,
    "Nithi":35000,
    "Devi":40000,
    "Chandar":28000,
    "Sakthi":50000
}
for name, salary in employees.items():
    if salary>30000:
        print(name,":",salary)
  #Write a program to merge two dictionaries. If the same key appears in both dictionaries, keep the value from the second dictionary.      
  dict1={
    "Name":"Nithi",
    "age":22,
    "city":"Chennai"
  }
  dict1={
    "Name":"Devi",
    "age":25,
    "city":"Banglore"
  }
  dict1.update(dict2)
  print(dict1)
  #Given a dictionary of item names and quantities, use a dictionary method to remove an item entered by the user. Handle the case where the item is not present.
  items={
    "Rice":10,
    "Sugar":5,
    "Wheat":8,
    "Oil":4
  }
  items=input("Enter item Name")
  result=items.pop(item,None)
  if result is not None:
    print("Item Removed Suessfully")
else:
    print("Item Not Found")
print(items)
#Create a dictionary of subjects and marks. Calculate and print the total marks and average mark.
marks={
    "Tamil":80,
    "English":75,
    "Python":90,
    "Maths":85
}
total=sum(marks.values())
average=total/len(marks)
print("Total Marks:",total)
print("Average Marks:",average)
#Write a program that finds and prints the key with the highest value in a dictionary of student marks.
students={
    "Arun":75,
    "Kumar":90,
    "Ravi":85,
    "Bala":95,
    "Kavin"
}
topper=max(students,key=students.get)
highest_mark=students[topper]
print("Topper:",topper)
print("Highest Marks:",highest_mark)
#Create a phone book using a dictionary. Allow the user to add a contact, search for a contact, update a phone number, and delete a contact.
contacts={
    "Arun":8181818181
    "Kumar":7171717171
    "kavin":9191919191

}
contacts["Ravi"]=8787878787
print(contacts.get("Arun","Contact Not Found"))
contacts["Kumar"]=7272727272
contacts.pop["Arun",None]
print(contacts)
#Given a dictionary of products and prices, use items() to print each product and price in the format: Product: _, Price: _.
products={
    "Laptop":45000,
    "Mouse":500,
    "Keyboard"1000
}
for product,price inproducts.items():
    print(f"Product:{product},Price:{price}")
#13. Write a program that uses setdefault() to group the following names by their first letter: Arun, Anu, Bala, Banu, Kavin, Kumar.
names=["Arun","Anu","Bala","Kavin","Kumar"]
groups={}
for name in names:
    first_letter=name[0]
    groups.setdefault(first_letter,[]).append(name)
print(groups)
#14. Create a dictionary from two lists: one containing employee names and another containing their departments. Use zip() to build the dictionary.
names=["Arun","Bala","Kumar"]
departments=["HR","IT","Sales"]
employees=dict(zip(names,departments))
print(employees)
#15. Write a program to invert a dictionary so that its values become keys and its keys become values. Assume all original values are unique.
student={
    "Arun":80,
    "Bala":90,
    "Kumar":85
}
reveresed_dict={}
for key, value in students.items():
    reversed_dict[value]=key
print(reversed_dict)
#Given a dictionary containing student names and marks, create a new dictionary containing only students who scored 50 or more.
students={
    "Arun":80
    "Bala":45
    "Kumar":90
    "Ravi":35
}
passed={}
for names,marks in students.items():
    if mark>=50:
        passed[name]=mark
print(passed)
#Write a program that stores shopping-cart items and quantities in a dictionary. Let the user add quantities to an existing item or add a new item, then display the cart total quantity.
cart={
    "Rice":2
    "Sugar":1
}
item=input("Enter a Item:")
quantity=int(input("Enter quantity:"))
if item in cart:
    cart[item]+=quantity
else:
    cart[item]=quantity
print(cart)
print("Total Quantity:",sum(cart.values()))
#18. Create a nested dictionary for three students. Each student should have a name, age, and marks dictionary. Print the mark scored by each student in Mathematics.
student={
    "student1":{
    "name":"Arun",
    "age":20,
    "marks":{"maths":90,"python:85"}
    },
    "student1":{
    "name":"Devi",
    "age":22,
    "marks":{"maths":80,"python:75"}
    },
    "student1":{
    "name":"krishna",
    "age":20,
    "marks":{"maths":95,"python:90"}
    },

}
for student in students.values():
    print(student["name"],student["marks"],["Maths"])
#Write a function called count_vowels(text) that returns a dictionary containing the count of each vowel in the given text. Do not include vowels with a count of zero.
def count_vowels(text):
    vowels={}
    for char in text.lower():
        if char in "aeiou":
            vowels[char]=vowels.get(char,0)+1
        return vowels
result=count_vowels("Hello Python Programming")
print(result)
