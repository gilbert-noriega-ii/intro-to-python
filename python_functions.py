#Use print() in combination with type() to print out the type of var1.
#Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
#Use int() to convert var2 to an integer. Store the output as out2.

var1 = [1, 2, 3, 4]
var2 = True

print(type(var1))
print(len(var1))

print(type(var2))

out2 = int(var2)

#Use + to merge the contents of first and second into a new list: full.
#Call sorted() on full and specify the reverse argument to be True. Save the sorted list as full_sorted.
#Finish off by printing out full_sorted.

first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

full = first + second

full_sorted = sorted(full, reverse = True)

print(full_sorted)

#Use the upper() method on place and store the result in place_up. Use the syntax for calling methods that you learned in the previous video.
#Print out place and place_up. Did both change?
#Print out the number of o's on the variable place by calling count() on place and passing the letter 'o' as an input to the method. We're talking about the variable place, not the word "place"!

place = "poolhouse"

place_up = place.upper()

print(place)
print(place_up)

print(place.count('o'))

#Use the index() method to get the index of the element in areas that is equal to 20.0. Print out this index.
#Call count() on areas to find out how many times 9.50 appears in the list. Again, simply print out this number.

areas = [11.25, 18.0, 20.0, 10.75, 9.50]

print(areas.index(20.0))

print(areas.count(9.50))

#Use append() twice to add the size of the poolhouse and the garage again: 24.5 and 15.45, respectively. Make sure to add them in this order.
#Print out areas
#Use the reverse() method to reverse the order of the elements in areas.
#Print out areas once more.

areas = [11.25, 18.0, 20.0, 10.75, 9.50]

areas.append(24.5)
areas.append(15.45)

print(areas)

areas.reverse()

print(areas)

#Import the math package. Now you can access the constant pi with math.pi.
#Calculate the circumference of the circle and store it in C.
#Calculate the area of the circle and store it in A.

r = 0.43

import math

C = 2*math.pi*r

A = math.pi*r*r

print("Circumference: " + str(C))
print("Area: " + str(A))

#Perform a selective import from the math package where you only import the radians function.
#Calculate the distance travelled by the Moon over 12 degrees of its orbit. Assign the result to dist. You can calculate this as r * phi, where r is the radius and phi is the angle in radians. To convert an angle in degrees to an angle in radians, use the radians() function, which you just imported.
#Print out dist.

r = 192500

from math import radians

dist = radians(r*12)

print(dist)