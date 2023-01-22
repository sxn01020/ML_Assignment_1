#Creating an empty dictionary called dog
dog={}

#Adding data to the dog dictionary
dog["name"]="Flash"
dog["color"]="brown"
dog["breed"]="beagle"
dog["legs"]=4
dog["age"]=2
print("Dog dictionary after adding keys and values is: ",dog)

#Creating a student dictionary and adding the data
student={}
student["first_name"]="Sriram"
student["last_name"]="Nalabolu"
student["geneder"]="male"
student["age"]=25
student["marital status"]="single"
student["skills"]=["python","big data","devops","cloud"]
student["country"]="United States of America"
student["city"]="Kansas"
student["address"]="6600 W 140th Street"
print("Student dictionary after adding keys and values is: ",student)

#Printing the length of student dictionary
length=len(student)
print("Length of student dictionary is: ",length)

#Printing the value of skills and checking the data type of skills
print("Value of skills is: ",student["skills"])
print("Data Type of skills is: ",type(student["skills"]))

#Modifying the skills values by adding two skills
student["skills"].append("java")
student["skills"].append("ansible")
print("Skills values after adding two skills is: ",student["skills"])

#Printing the Dog dictionary keys and values as a list
print("Dog keys as a list is: ",dog.keys())
print("Dog values as a list is: ",dog.values())

#Printing the Student dictionary keys and values as a list
print("Student keys as a list is: ",student.keys())
print("Student values as a list is: ",student.values())