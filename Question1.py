import math #Importing math package

#list of 10 student's ages
ages= [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#sorting the list of ages
ages.sort()
print("Sorted ages list is: ",ages)

#Finding the minimum age from the list of ages
min_age=min(ages)
print("Minimum age from the sorted list is: ",min_age)

#Finding the maximum age from the list of ages
max_age=max(ages)
print("Maximum age from the sorted list is: ",max_age)

#Adding minimum and maximum ages again to the list of ages
ages.append(min_age)
ages.append(max_age)
print("Student's ages list after adding minimum and maximum ages back to the list: ",ages)

#Finding the median age from the list
length=len(ages)
#Finding the median age from the list when the length of the list is odd
if length%2!=0:
    median=length//2  #length of the list
    median=math.ceil(median)  #calculating the index of the median
    print("Median age from the list of ages is: ",ages[median])  #printing the median age from the list when the length of the list is odd
# Finding the median age from the list when the length of the list is even
else:
    median=length//2  #length of the list
    print("Median age from the list of ages is: ",(ages[median-1]+ages[median])/2)  #printing the median age from the list when the length of the list is even

#Finding the average age from the list of ages
avg=sum(ages)/len(ages)
print("Average age from the list og ages is: ",avg)

#Finding the range of the ages
range=max_age-min_age
print("Range of the ages is: ",range)