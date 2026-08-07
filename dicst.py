student= {
    "name":"ayush",
    "age": 20 ,
    "marks": 80 ,
    "course" : "bca"
}

print ("Students:",student)

print ("name:",student["name"])
print("course:",student["course"])

student["marks"] = 80
print("Updated marks:", student["marks"])

student["city"] = "Ramgarh"
print("Updated dictionary:", student)

del student["age"]
print("After deleting age:", student)



