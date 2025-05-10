num= int(input("Enter a number: "))

if num == 0:
    print("Zero")
elif num > 0:
    print("positive")
else:
    print("negative")

# ============================================

movies= ["movie01", "movie02", "movie03"]
movies.append("movie04")
movies[1] = "movie05"

print(movies)

# ===============================================

for i in range(1, 11):
    print(i)
    
i=10    
while i>=1:
    print(i)
    i-=1
    
for i in range(21):
    if i%2 == 0:
        print(i)
    else:
        continue
    
# =========================================

def squre(num):
    return num**2

num= int(input("enter the num: "))
print(f"squre of number {num} is, {squre(num)}")

def greet(name="umang", age=20):
    print(f"Hello {name}! You are {age} years old.")
    
name = input("enter name: ")
age = int(input("enter age: "))

greet(age, name)

# ===========================================

fname= "Umang Dalvadi"

print(fname.upper())
print(fname[:5])
print(len(fname.replace(" ", "")))

mail= input("enter your mail: ")
print(mail.endswith("@gmail.com"))

# ===================================================

fruits= ["Fig", "Apple", "Avocados", "Pear", "Banana"]

for fruit in fruits:
    if len(fruit) > 5:
        print(fruit)


numbers = []
for i in range(3):
    item= int(input(f"enter {i} number: "))
    numbers.append(item)

avg= sum(numbers)/len(numbers)
print("Average:", avg)

# ==================================

dic= {
    "name": "Umang Dalvadi",
    "age": 20,
    "courses": ["p", "c", "m"],
    "graduation_year":2025
}

dic["graduation_year"]= 2026
dic["internship_done"]=True

for k,v in dic.items():
    print(f"{k} -> {v}")
    
# ====================================

def create_user(name, age, city):
    user= {
        "name": name,
        "age": age,
        "city": city
    }
    return user

def update_city(user, city):
    user["city"] = city
    return user

def show_profile(user):
    for k, v in user.items():
        print(f"{k} -> {v}")

    
def register_user():
    name = input("enter name: ")
    age = int(input("enter age: "))
    city = input("enter city: ")
    
    return create_user(name, age, city)

new_user= register_user()
print("User registered:", new_user)

updated_user= update_city(new_user, "Ahmedabad")

show_profile(updated_user)

# =======================================

import json

try:
    name = input("enter name: ")
    age = int(input("enter age: "))
    city = input("enter city: ")
    user = {
        name,
        age,
        city
    }
    
    with open("user.json", "w") as f:
        json.dump(user, f)
        
    with open("user.json", "r") as r:
        show_profile(json.load(r))
        
except ValueError:
    print(f"error: {ValueError}")
    
    



    
    

