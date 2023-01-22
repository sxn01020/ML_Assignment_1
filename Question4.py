it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Finding the length of it_companies
print("Length of it_companies set is: ",len(it_companies))

#Adding Twitter to it_companies
it_companies.add("Twitter")
print("it_companies set after adding twitter to it is: ",it_companies)

#Inserting multiple it companies to the set it_companies
it_companies.update({"Tesla","Cap Gemini","Tech Mahindra","Accenture"})
print("it_companies set after adding multiple companies to it is: ",it_companies)

#Removing one of the companies from the set it_companies
it_companies.remove("Cap Gemini")
print("it_companies set after removing Cap Gemini from the set is: ",it_companies)

#Removing one of the companies from the set it_companies
it_companies.discard("Cap Gemini")
#Discard will not throw an error even if the element is not present in the set whereas Remove will throw an error.

#Joining A and B sets
print("Set after joining A and B sets is: ",A.union(B))

#Finding A intersection B
print("Set after intersection of A and B sets is: ",A.intersection(B))

#Finding if A is a subset of B
print("A is subset of B: ",A.issubset(B))

#Finding if A and B are disjoint sets
print("A is disjoint of B: ",A.isdisjoint(B))

#Joining A with B and B with A
print("set after joining A with B: ",A.union(B))
print("set after joining B with A: ",B.union(A))

#Finding the symmetric difference between A and B
print("Symmetric difference between A and B is: ",A.symmetric_difference(B))

#Deleting the sets completely
print(A.clear())
print(B.clear())
print(it_companies.clear())

#Converting the age list to set and comparing the length of age set and age list
print("Age set after converting from List to set is: ",set(age))
print("Length of age set: ",len(set(age)))
print("Length of age list: ",len(age))