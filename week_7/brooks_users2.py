"""

    Title: Exercise 7.3 - Python with MongoDB, Part 2
    Author: Krasso
    Date: 04/26/2023
    Description: "Using Python with MongoDB to add, modify and delete a 
    document."

"""

# Using the “Python Guide” document I provided as a guide, build a 
# Python program that connects to your web335DB database.

# import the MongoClient
from pymongo import MongoClient
import datetime

# build a connection string to connect to
client = MongoClient('mongodb+srv://web335_user:s3cret@bellevueuniversity.kqpr8ra.mongodb.net/?retryWrites=true&w=majority')

print(f"\n{client}")

# configure a variable to access the web335DB
db = client['web335DB']



# Write the Python code to create a new user document.
addId = db.users.insert_one({ 'firstName': 'Franz', 'lastName': 'Schubert', 'employeeId': '1015', 'email': '', 'dateCreated': datetime.datetime.utcnow() }).inserted_id

schubert = db.users.find_one({ 'lastName': 'Schubert'})

# Write the Python code to display the newly created document.
print(f'\n{schubert}')




# Write the Python code to update the email address of the document you created
db.users.update_one({ 'lastName': 'Schubert'}, { '$set': { 'email': 'fschubert@mail.com'}})

schubert2 = db.users.find_one({ 'lastName': 'Schubert'})

# Write the Python code to display the updated document.
print(f'\n{schubert2}')




# Write the Python code to delete the document you created
db.users.delete_one({ 'lastName': 'Schubert'})

schubert3 = db.users.find_one({ 'lastName': 'Schubert'})

# Write the Python code to prove the document was deleted.
print(f'\n{schubert3}')

