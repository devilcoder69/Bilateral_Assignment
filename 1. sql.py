# Prog. to create table
# make sure you have already created a database in mysql
# Change the database name 
# Run the prog
# Enter the table name 


import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host = "localhost", 
                                    port = "3306", 
                                    user = "root", 
                                    password = "root",
                                    database = "database1") 
        
        table = input('Enter the name of table to create a table :- ')
        query1 = f'create table if not exists {table}(Queue int)'
        cur1 = self.con.cursor()
        cur1.execute(query1)
    
helper = DBHelper()




