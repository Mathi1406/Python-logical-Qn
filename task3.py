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
    