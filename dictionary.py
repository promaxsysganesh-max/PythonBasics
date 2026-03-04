student = {
    "name": "Ganesh",
    "age": 22,
    "city": "Pune"
}

#accessing
print(student["name"])   # Ganesh
print(student["age"])    # 22

print(student.get("name"))


student["age"] = 23          # update
student["course"] = "Python" # add

student.pop("city") #remove


for key, value in student.items():
    print(key, ":", value)