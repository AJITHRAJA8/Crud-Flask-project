from flask import Flask,render_template,url_for,request,redirect
import mysql.connector

#Getting File Name
app=Flask(__name__)

#MySQL COnnection
con=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Your_pass",
    database = "crud"
)
if con.is_connected():
    print("Connect Successfully")
else:
    print("Connection Has Problem")

#Loading Home Page
@app.route('/')
def home():
    res=con.cursor(dictionary=True)
    sql="select * from users"
    res.execute(sql)
    result = res.fetchall()
    return render_template("home.html",datas=result)

#new user Insert
@app.route('/add_user',methods=['GET','POST'])
def add_user():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        city=request.form['city']
        res=con.cursor(dictionary=True)
        sql="insert into users(name,age,city)values(%s,%s,%s)"
        values=(name,age,city)
        res.execute(sql,values)
        con.commit()
        return redirect(url_for('home'))
    return render_template("add_user.html")

#update user using ID
@app.route('/update',methods=['GET','POST'])
def update():
    return render_template("update")


if (__name__=="__main__"):
    app.run(debug=True)