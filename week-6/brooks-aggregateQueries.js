/*
============================================
; Title: Assignment 6.2 - Aggregate Queries
; Author: Professor Krasso 
; Date: 04/21/2023
; Modified By: Brooks
; Description:  MongoDB Shell queries. Create, Read, and Delete.
============================================
*/


// mongosh 'mongodb+srv://bellevueuniversity.kqpr8ra.mongodb.net/web335DB' --apiVersion 1 --username web335_user


// Created collections houses and students on MongoDB Atlas, gave permissions 
// to our web335_user.


// loading houses script.
load('houses.js')


// Write a query to show a list of documents in the houses collection
db.houses.find()


// Write a query to show a list of documents in the student’s collection
db.students.find()


// Write a query to add a document to the student’s collection
db.students.insertOne({'firstName': 'Brooke', 'lastName': 'Taylor', 'studentId': 's1019', 'houseId': 'h1009'})


// Next, write a query to prove the document was added to the user’s collection
db.students.findOne({'lastName': 'Taylor'})


// Write a query to delete the document you created
db.students.deleteOne({'lastName': 'Taylor'})


// Next, write a query to prove the document was added to the user’s collection
// *** believe directions were to prove document was deleted ***
db.students.find({'lastName': 'Taylor'})


// Write a query to show a list of students by house 
// (hint: use the lookup operation).
db.houses.aggregate([{ $lookup: { from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'students' }}])


// Write a query to show a list of students for house Gryffindor 
// (hint: use the lookup and match operations).  
db.houses.aggregate([{ $match: { houseId: 'h1007' }}, { $lookup: { from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'Gryffindor', }}])


// Write a query to show a list of students for the Eagle mascot
db.houses.aggregate([{ $match: { mascot: 'Eagle' }}, { $lookup: { from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'Ravenclaw', }}])

