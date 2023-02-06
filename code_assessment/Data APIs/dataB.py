import mysql.connector 

  

db = mysql.connector.connect( 

    host="localhost", 

    user="shreenivas", 

    password="shree123", 

    database="FinCompany"
) 

  
# getting the cursor by cursor() method 

mycursor = db.cursor() 

query_1 = "ALTER TABLE company ADD revenue text;"

query_2 = "insert into company (comp_nm text, comp_id integer primary key, open float(3), high float(3), low float(3), close float(3), adjclse float(3), volume integer, revenue text) values ('IBM', 0001, 127.09, 127.09, 126.07, 188.99, 187.99, 34548000, '19B');"

  
# execute the queries 
mycursor.execute(query_1) 
mycursor.execute(query_2) 

  

mycursor.execute("select * from persons;") 

myresult = mycursor.fetchall() 

for row in myresult: 

    print(row) 

  
db.commit() 

  
# close the Connection 
db.close()