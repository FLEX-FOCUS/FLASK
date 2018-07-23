This is my first time write RESTful, enjoyed a lot!

run the program and go to http://127.0.0.1/, should see a welcome page of "Welcome to DataBase!"

type http://127.0.0.1/find/id=1 in the bar should return all rows with ID equal to 1

http://127.0.0.1/find/description=Cesna%20120 will return objects with description name Cesna 120

http://127.0.0.1/add/id=1&description=woody&datetime=2016-10-12&longitude=1&latitude=-1&elevation=1

will add a new row with following information to the database

id = 1 description = woody datetime = 2016-10-12 longitude = 1 latitude = -1 elevation =1


http://127.0.0.1/delete/id=1&datetime=2016-10-12 will delete rows with id =1 and the datetime = 2016-10-12


BTW, because the original date type in the input.docx is hard to find the datatype, and I assume it is not the key point of the project thereby I modifed those information.
I dont want to spend too much time dealing with a datatype, I have only 2 days and there are also other interviews need to prepare :)

The orignal is 2016-10-12T12:00:00-05:00, which is a datetime I have never seen before, I delete those after T to focus on the FLASK part.


I did not do the page part, feel like it is more about the HTML and can cause a lot of new troubles. 


Data validation is enforced in this way:

http://127.0.0.1/find/id=helloworld

This will return "It needs to be an integer!" because the id of a row cannot be "Hello World"



Thanks for providing this learning oppotunity, learned a lot about python, FLASK and SQLite!
