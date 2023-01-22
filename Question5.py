import math #importing math package

radius=30 #initalizing radius as 30

#Calculating the area of circle and storing it in _area_of_circle variable
_area_of_circle=int((math.pi)*(radius**2))
print("Area of circle is: ",_area_of_circle)

#Calculating the perimeter of circle and storing it in _circum_of_circle
_circum_of_circle=int(2*math.pi*radius)
print("Circumference of circle is: ",_circum_of_circle)

#Taking the user input for radius and storing it in radius variable
radius=int(input("Enter the radius of circle: "))

#Calculating the area using the user's input radius and storing it in _area_of_circle variable
_area_of_circle=int((math.pi)*(radius**2))
print("Area of the circle using user's input radius is: ",_area_of_circle)