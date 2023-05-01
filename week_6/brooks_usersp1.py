"""

    Title: Exercise 6.3 - Python with MongoDB, Part 1
    Author: Brooks
    Date: 04/21/2023
    Description: "Python connect with MongoDB and basic queries."

"""

# Using the “Python Guide” document I provided as a guide, build a 
# Python program that connects to your web335DB database.

# import the MongoClient
from pymongo import MongoClient

# build a connection string to connect to
client = MongoClient('mongodb+srv://web335_user:s3cret@bellevueuniversity.kqpr8ra.mongodb.net/?retryWrites=true&w=majority')

print(client)

# configure a variable to access the web335DB
db = client['web335DB']


# Write the Python code to display all documents in the user’s collection.
print('\nListing out all documents in collection.\n')

for user in db.users.find():

    print(user)


# Write the Python code to display a document where the employeeId is 1011.
print('\nDisplaying employeeId 1011.')

print(db.users.find_one({'employeeId': '1011'}))


# Write the Python code to display a document where the lastName is Mozart. 
print('\nDisplaying user with lastName of Mozart.')

print(db.users.find_one({'lastName': 'Mozart'}))

