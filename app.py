from flask import Flask,render_template,url_for
import mysql.connector

#Getting File Name
app=Flask(__name__)

#MySQL COnnection
con=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@Ajith@9751",
    database = "crud"
)
if con.is_connected():
    print("Connect Successfully")
else:
    print("Connection Has Problem")

#Loading Home Page
@app.route('/')
def Home():
    res=con.cursor(dictionary=True)
    sql="select * from users"
    res.execute(sql)
    result = res.fetchall()
    return render_template("home.html",datas=result)

#new user Insert
@app.route('/add_user',methods=['GET','POST'])
def add_user():
    return render_template("add_user.html")


if (__name__=="__main__"):
    app.run(debug=True)