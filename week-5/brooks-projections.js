/*
============================================
; Title: Exercise 5.2 - Projections
; Author: Professor Krasso 
; Date: 04/14/2023
; Modified By: Brooks
; Description: MongoDB Shell queries. Create, Read, and Update. 
============================================
*/
 
// mongosh "mongodb+srv://bellevueuniversity.kqpr8ra.mongodb.net/web335DB" --apiVersion 1 --username web335_user


// Write a query to add a new user to the user’s collection.
// Make sure the fields in the new document match 
// the existing fields in the user’s collection.

// add Chopin
db.users.insertOne({"firstName": "Frederic", "lastName": "Chopin", "employeeId": "1013", "email": "fchopin@me.com", "dateCreated": new Date()})

// add Tchaikovsky
db.users.insertOne({"firstName": "Pyotr", "lastName": "Tchaikovsky", "employeeId": "1014", "email": "ptchaikovsky@me.com", "dateCreated": new Date()});


// Write a query to update Mozart’s email address to mozart@me.com
try { db.users.updateOne({ 'lastName': 'Mozart'}, { $set: { 'email': 'mozart@me.com'}})} catch (e) { print(e); }

// Next, write a query to prove the email address was updated
db.users.findOne({ 'lastName': 'Mozart' })


// Write a query to list all documents in the user’s collection.  
// Use projections to only display the firstName, lastName, 
// and email fields.  
db.users.aggregate({ $project: { firstName: 1, lastName: 1, email: 1}})

