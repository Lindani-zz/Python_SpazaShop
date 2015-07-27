from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'green_grocer'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'spaza'

mysql = MySQL(app)

@app.route("/")
def products():
    cur = mysql.get_db().cursor()
    cur.execute('''SELECT Name,SUM(Sales_price*Qty) AS TotalEarnings from Sales INNER JOIN Products ON Sales.Product_id = Products.Id GROUP BY Name ORDER BY TotalEarnings''')
    products = [dict(TotalEarnings=row[1], Name=row[0]) for row in cur.fetchall()]
    """mysql.connection.commit()"""
    return render_template('menu.html', products=products)



if __name__ == '__main__':
   
    app.run(debug=True,
      port=int("8040")) 

