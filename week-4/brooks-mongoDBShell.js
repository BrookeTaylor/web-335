/*
============================================
; Title: Exercise 4.3 - MongoDB Shell
; Author: Professor Krasso 
; Date: 04/07/2023
; Modified By: Brooks
; Description: For this week's assignment you will be working with 
; the MongoDB shell to build and execute queries. 
============================================
*/ 


// Using the WEB 335 mongosh Guide, load the user.js script from 
// week four (4) of the courses GitHub repository.
load('users.js')


// Write a query to display all of the documents in the user’s 
// collection. 
db.users.find()


// Write a query find the user with an email address of jbach@me.com.
db.users.findOne({'email': 'jbach@me.com'})


// Write a query to find a user with the last name of Mozart.   
db.users.findOne({'lastName': 'Mozart'})


// Write a query to find a user with a first name of Richard. 
db.users.findOne({'firstName': 'Richard'})


// Write a query to find a user with an employeeId of 1010.  
db.users.findOne({'employeeId': '1010'}) 

