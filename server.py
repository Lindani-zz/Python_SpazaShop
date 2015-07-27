import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="green_grocer", # your username
                      passwd="password", # your password
                      db="spaza") # name of the data base
cursor = db.cursor ()


cursor.execute ("SELECT SUM(Qty) AS TotalQty , Product_Id, Name from Sales s INNER JOIN Products p ON s.Product_Id = p.Id GROUP BY Name ")
data = cursor.fetchall ()
for row in data:
    print row[0], row[2]

cursor.execute ("SELECT  Categories.Name, sum(Sales.Qty) AS TotalQty from Sales INNER JOIN Products ON Sales.Product_id = Products.Id INNER JOIN Categories ON Products.Category_id = Categories.Id GROUP BY Categories.Name")
data = cursor.fetchall ()
for row in data:
    print 'Category list' + ' '+row[0],row[1]

cursor.execute ("SELECT * FROM Products")
data = cursor.fetchall ()
for row in data:
    print 'Product list' + ' '+row[1]

cursor.close ()


db.close ()