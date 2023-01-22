#Creating tuples containing names of sisters and brothers
brothers=("lakshman","bharath")
sisters=("sravani","harivina")
print("My Brothers are: ",brothers)
print("My Sisters are: ",sisters)

#Joining brothers and sisters tuples into siblings tuple
siblings=brothers+sisters
print("My Siblings are: ",siblings)

#Calculating the total number of siblings
print("Total number of siblings I have are: ",len(siblings))

#Adding mother, father and sublings to family_members tuple
family_members=("Ravi","Gayathri")+siblings
print("My family members are: ",family_members)