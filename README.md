# Bilateral_Assignment
Question :-

Make Folders named Processing,queue and processed and Write a code that makes a file(txt) every second in the Processing folder, 
picks up all files from processing and moves all the files to queue every 5 seconds and picks file from the queue folder,
updates a column in MySQL/mongoDB table as 0/1 and moves the file to the Processed folder.   
Also, make sure no files are moved from Processing to queue until queue folder is empty

Solution 1 :- 
1. First run "1.sql.py" to create table in precreated database.
2. After that run "2.main.py" and input the table name and  no of files you want to create.

Solution 2 :- 
run "main.py"
