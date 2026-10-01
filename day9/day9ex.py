"""
Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries
"""
tenting = ["campout", "roll call", "line monitor", "game wristband", "rivalry game"]

c = len(tenting[-3])#len của chữ string

d = tenting[0][3] * 3#p nhân 3 = ppp
e = tenting[0:2] + tenting[4:]

print(d)

print(e)

print(c)

# 1
dog={}

#2
dog["name"] = "Bun"
dog["color"] = "yellow"
dog["breed"] = "Bug"
dog["legs"] = 4
dog["age"] = 3

print(dog)

#3
student={
    "first_name": "Quan",
    "last_name": "Le",
    "gender": "male",
    "age": 20,
    "marital_status": "single",
    "skills": ["Python", "Excel","Accounting"],
    "country": "Germany",
    "city": "Dortmund",
    "address": "Dortmund"
}

print(student)

#4
print(len(student))

#5
print(student["skills"])
print(type(student["skills"]))

#6
student["skills"].append("presentation")

print(student)

#7

student_values=student.values()

print(student_values)

print(type(student_values))

#8
student_keys=student.keys()

print(student_keys)

print(type(student_keys))

#9
student_items=list(student.items())



print(student_items)

#10
del student["address"]

print(student)

#11
del dog

print(dog)









