"""
    Title: Exercise 3.3 - Python Variables and Functions
    Author: Prof Krasso
    Date: 04/02/2023
    Description: Experimenting with Python 
    variables and functions.  

"""

# Create a function named add with two parameters 
# and in the body of the method return the total.
def add(x, y):
    return x + y


# Create a function named subtract with 
# two parameters and in the body of the 
# method return the subtracted total. 
def subtract(x, y):
    return x - y



# Create a function named divide with 
# two parameters and in the body of the 
# method return the divided total.
def divide(x, y):
    return x / y


# Create a function named multiply with 
# two parameters and in the body of the 
# method return the multiplied total.
def multiply(x, y):
    return x * y



# Create variables to test each function
b = 2 
d = 4
f = 6
h = 8
j = 10



# Use a variable to build a string for the results.
output = (f"{d} + {d} is {add(d,d)}\n{j} - {f} is {subtract(j,f)}\n{h} / {b} is {divide(h,b)}\n{j} * {b} is {multiply(j,b)}")




# Call each function passing in the variables 
# created in step 6 and print the results to 
# the console window using an output variable 
print(output)



