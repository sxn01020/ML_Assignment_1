weights=[] #creating weights list
kilograms=[] #creating kilograms list

#Taking the number of students from user
N=int(input("Enter the number of students: "))

#Taking the weights of these students from user in lb
for i in range(N):
    weights.append(int(input("Enter the weight of student{}: ".format(i+1))))

print("Weight of students in lb is: ",weights) #printing the list of weights in lb

#Calculating kilograms using weights in lb and appending them to a list
for i in weights:
    kilograms.append(round(float(i/2.2046),2))

#printing the list of weights in kilograms
print("List of weights of students in kilograms is: ",kilograms)