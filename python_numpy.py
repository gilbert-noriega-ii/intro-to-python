import numpy as np

#Import the numpy package as np, so that you can refer to numpy with np.
#Use np.array() to create a numpy array from baseball. Name this array np_baseball.
#Print out the type of np_baseball to check that you got it right.

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

np_baseball = np.array(baseball)

print(type(np_baseball))


#Create a numpy array from height_in. Name this new array np_height_in.
#Print np_height_in.
#Multiply np_height_in with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
#Print out np_height_m and check if the output makes sense.

np_height_in = np.array(height_in)

print(np_height_in)

np_height_m = np_height_in * .0254

print(np_height_m)


#Create a numpy array from the weight_lb list with the correct units. Multiply by 0.453592 to go from pounds to kilograms. Store the resulting numpy array as np_weight_kg.
#Use np_height_m and np_weight_kg to calculate the BMI of each player. Use the following equation:
#BMI = weight(kg)/height(m)^2
#Save the resulting numpy array as bmi.
#Print out bmi.

np_height_m = np.array(height_in) * 0.0254

np_weight_kg = np.array(weight_lb) * .453592

bmi = np_weight_kg / np_height_m ** 2

print(bmi)


#Create a boolean numpy array: the element of the array should be True if the corresponding baseball player's BMI is below 21. You can use the < operator for this. Name the array light.
#Print the array light.
#Print out a numpy array with the BMIs of all baseball players whose BMI is below 21. Use light inside square brackets to do a selection on the bmi array.

np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

light = np.array(bmi < 21)

print(light)

print(bmi[light])

#Subset np_weight_lb by printing out the element at index 50.
#Print out a sub-array of np_height_in that contains the elements at index 100 up to and including index 110.

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

print(np_weight_lb[50])

print(np_height_in[100:111])


#Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
#Print out the type of np_baseball.
#Print out the shape attribute of np_baseball. Use np_baseball.shape.

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

np_baseball = np.array(baseball)

print(type(np_baseball))

print(np_baseball.shape)


#Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
#Print out the shape attribute of np_baseball

np_baseball = np.array(baseball)

print(np_baseball.shape)


#Print out the 50th row of np_baseball.
#Make a new variable, np_weight_lb, containing the entire second column of np_baseball.
#Select the height (first column) of the 124th baseball player in np_baseball and print it out.

np_baseball = np.array(baseball)

print(np_baseball[49, :])

np_weight_lb = np_baseball[:, 1]

print(np_baseball[123,0])


#You managed to get hold of the changes in height, weight and age of all baseball players. It is available as a 2D numpy array, updated. Add np_baseball and updated and print out the result.
#You want to convert the units of height and weight to metric (meters and kilograms respectively). As a first step, create a numpy array with three values: 0.0254, 0.453592 and 1. Name this array conversion.
#Multiply np_baseball with conversion and print out the result.

np_baseball = np.array(baseball)

print(np_baseball + updated)

conversion = np.array([0.0254, 0.453592, 1])

print(np_baseball * conversion)


#Create numpy array np_height_in that is equal to first column of np_baseball.
#Print out the mean of np_height_in.
#Print out the median of np_height_in.

np_height_in = np_baseball[:, 0]

print(np_height_in.mean())

print(np.median(np_height_in))


#The code to print out the mean height is already included. Complete the code for the median height. Replace None with the correct code.
#Use np.std() on the first column of np_baseball to calculate stddev. Replace None with the correct code.
#Do big players tend to be heavier? Use np.corrcoef() to store the correlation between the first and second column of np_baseball in corr. Replace None with the correct code.

avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

med = np.median(np_baseball[:,0])
print("Median: " + str(med))

stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

corr = np.corrcoef(np_baseball[:, 0], np_baseball[:,1])
print("Correlation: " + str(corr))


#Convert heights and positions, which are regular lists, to numpy arrays. Call them np_heights and np_positions.
#Extract all the heights of the goalkeepers. You can use a little trick here: use np_positions == 'GK' as an index for np_heights. Assign the result to gk_heights.
#Extract all the heights of all the other players. This time use np_positions != 'GK' as an index for np_heights. Assign the result to other_heights.
#Print out the median height of the goalkeepers using np.median(). Replace None with the correct code.
#Do the same for the other players. Print out their median height. Replace None with the correct code.

np_positions = np.array(positions)
np_heights = np.array(heights)

gk_heights = np_heights[np_positions == 'GK']
other_heights = np_heights[np_positions != 'GK']

print("Median height of goalkeepers: " + str(np.median(gk_heights)))
print("Median height of other players: " + str(np.median(other_heights)))