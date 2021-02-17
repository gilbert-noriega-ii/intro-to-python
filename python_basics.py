#Suppose you have $100, which you can invest with a 10% return each year. After one year, it's 
#100×1.1=110 dollars, and after two years it's 100×1.1×1.1=121. Add code to calculate how much money you end up with after 7 years, and print the result.

print(100*1.1**7)

#Create a variable savings with the value 100.
#Check out this variable by typing print(savings) in the script.

savings = 100
print(savings)

#Create a variable growth_multiplier, equal to 1.1.
#Create a variable, result, equal to the amount of money you saved after 7 years.
#Print out the value of result.

savings = 100
growth_multiplier = 1.1
result = 100 * 1.1**7
print(result)

#Create a new string, desc, with the value "compound interest".
#Create a new boolean, profitable, with the value True.

desc = 'compound interest'
profitable = True

#Calculate the product of savings and growth_multiplier. Store the result in year1.
#What do you think the resulting type will be? Find out by printing out the type of year1.
#Calculate the sum of desc and desc and store the result in a new variable doubledesc.
#Print out doubledesc.

savings = 100
growth_multiplier = 1.1
desc = "compound interest"
year1 = savings*growth_multiplier
print(type(year1))
doubledesc = desc +desc
print(doubledesc)

#Hit Run Code to run the code. Try to understand the error message.
#Fix the code such that the printout runs without errors; use the function str() to convert the variables to strings.
#Convert the variable pi_string to a float and store this float as a new variable, pi_float.

savings = 100
result = 100 * 1.10 ** 7
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")
pi_string = "3.1415926"
pi_float = float(pi_string)

