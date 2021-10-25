# Assignment
# 0. First run the sql.py prog
# 1. Run the prog
# 2. Enter the table name you created before
# 3. Enter the no. of files to create

import os
import time
import shutil
import mysql.connector as connector

############# to connect mysql to python prog ############
con = connector.connect(host = "localhost", 
                                    port = "3306", 
                                    user = "root", 
                                    password = "root", 
                                    database = "testdatabase")

############# to insert status in table ############
def insert_status(status):
    query1 = f"insert into {table_name}(Queue) values({status})"
    cur = con.cursor()
    cur.execute(query1)
    con.commit()

############# to create folders ############
folders = ['Processing','Processed','Queue']
try:
    for folder in folders:
        path = os.path.join('',folder)
        os.mkdir(path)
except OSError as error: 
    print(error)

############# user inputs ############
table_name = input('Enter name of the table :- ')
no_of_files = int(input('Enter the no of files :- '))

counter = 1

############ func to create files in processing folder ############
def create_file_in_processing(n):
    for i in range (1,n+1):
        global counter
        path = 'Processing'
        file = f'{i}.txt'
        with open(os.path.join(path,file), 'w') as fp:
            time.sleep(1)
        if counter == 5:
            move_file_from_processing_to_queue()
            # time.sleep(1)
            move_file_from_queue_to_processed()
        elif i==n:
            move_file_from_processing_to_queue()
            # time.sleep(1)
            move_file_from_queue_to_processed()
        else:
            counter += 1

############# func to move file from processing to queue folder ############
def move_file_from_processing_to_queue():
    global counter
    source_dir = 'Processing'
    target_dir = 'Queue'
    file_names = os.listdir(source_dir)
    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)
        counter = 1
    insert_status(1)

############# func to move file from queue to processed folder ############
def move_file_from_queue_to_processed():
    source_dir = 'Queue'
    target_dir = 'Processed'
    file_names = os.listdir(source_dir)
    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)
    insert_status(0)
        

create_file_in_processing(no_of_files)




        














