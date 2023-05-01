"""

    Title: Exercise 5.3 - Python Conditionals, Lists, and Loops
    Author: Brooks
    Date: 04/15/2023
    Description: "Loop over a list of hobbies and days of the week."

"""

# Create a list of at least 5 hobbies.
hobbies = ['photography', 'skateboarding', 'hiking', 'reading', 'ice hockey']


# Use a for loop to iterate over the list of hobbies and print them 
# to the console window.
for hobby in hobbies:

    print(f"One of my favorite hobbies is {hobby}.")


# Create a list of days (Sunday through Saturday).
week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

# Use a for loop to iterate over the list of days
for i in week:

# and add an if…else statement to display what the day is.
    if i == (week[0]) or i == (week[6]):

# For Saturday and Sunday display a message indicating you 
# are off and should enjoy your hobbies.
        print(f"Congratulations, today is {i.title()}, you are off and should enjoy your hobbies!")

    else:

# For all other days display a message indicating it is a work day.
        print(f"Today is {i.title()}, it is a work day.")
