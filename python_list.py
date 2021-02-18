#Create a list, areas, that contains the area of the hallway (hall), kitchen (kit), living room (liv), bedroom (bed) and bathroom (bath), in this order. Use the predefined variables.
#Print areas with the print() function.

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

areas = [hall, kit, liv, bed, bath]

print(areas)

#Finish the code that creates the areas list. Build the list so that the list first contains the name of each room as a string and then its area. In other words, add the strings "hallway", "kitchen" and "bedroom" at the appropriate locations.
#Print areas again; is the printout more informative this time?

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

areas = ['hallway', hall, 'kitchen', kit, "living room", liv, 'bedroom', bed, "bathroom", bath]

print(areas)

#Finish the list of lists so that it also contains the bedroom and bathroom data. Make sure you enter these in order!
#Print out house; does this way of structuring your data make more sense?
#Print out the type of house. Are you still dealing with a list?

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ['bedroom', bed],
         ['bathroom', bath]]

print(house)

print(type(house))

#Print out the second element from the areas list (it has the value 11.25).
#Subset and print out the last element of areas, being 9.50. Using a negative index makes sense here!
#Select the number representing the area of the living room (20.0) and print it out.

areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

print(areas[1])

print(areas[-1])

print(areas[5])

#Using a combination of list subsetting and variable assignment, create a new variable, eat_sleep_area, that contains the sum of the area of the kitchen and the area of the bedroom.
#Print the new variable eat_sleep_area.

areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

eat_sleep_area = areas[3] + areas[7]

print(eat_sleep_area)

#Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
#Do a similar thing to create a new variable, upstairs, that contains the last 4 elements of areas.
#Print both downstairs and upstairs using print().

areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

downstairs = areas[:6]

upstairs = areas[-4:]

print(downstairs, upstairs)

#Update the area of the bathroom area to be 10.50 square meters instead of 9.50.
#Make the areas list more trendy! Change "living room" to "chill zone".

areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

areas[-1] = 10.50

areas[4] = 'chill zone'

#Use the + operator to paste the list ["poolhouse", 24.5] to the end of the areas list. Store the resulting list as areas_1.
#Further extend areas_1 by adding data on your garage. Add the string "garage" and float 15.45. Name the resulting list areas_2.

areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

areas_1 = areas + ["poolhouse", 24.5]

areas_2 = areas_1 + ['garage', 15.45]