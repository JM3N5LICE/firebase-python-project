# Firebase Python Attendance Project
# Overview

In this project I wanted to learn about cloud databases and their use case in local projects as a storage method. This is my first attempt to use and create a cloud database.

In this case, I used google firebase as my online table storage and I used python locally in Visual Studio Code. Students are able to be added to the table and require the attendance for a five day period as fields in order to be created in the table. Students can also be displayed, modified, and deleted from the table.

My purpose in writing this software was to learn how to use remote storage as a means to retain data for future programs. This is a relelvant skill to learn because most project developed professionally store their information remotely.


[Software Demo Video](http://youtu.be/oXKkyC5gNI4?hd=1)

# Cloud Database

I am using Firebase in the Google firestore as my database of choice. Instead of tables it uses collections, documents, and fields as the way it organizes data. 

In my database I use a collection called "students" and that collection contains the students names as they were inputted. Each name then has fields associated with them, which in this case are the school days of the week and associated values of yes and no. 

# Development Environment


The tools that I used were firebase, as stated above, python as the language I used to code, and visual studio code as the IDE for creating the code to manipulate the database. I also used a json file to contain the token to access the firebase and a .gitignore to keep that token off of Github, which I used as a remote repository for my code.

# Useful Websites


* [Firebase Documentation](https://firebase.google.com/docs/reference/admin/python)
* [Firebase Setup documentation](https://firebase.google.com/docs/firestore/quickstart#python)

# Future Work


* Use a timestamp to take daily attendance for all students added.
* A means to have teachers log in.
* Options to display more things about students such as student ID and grades.