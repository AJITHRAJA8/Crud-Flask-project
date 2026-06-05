from flask import Flask,render_template,url_for,request,redirect,flash
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
        flash("New User Added")
        return redirect(url_for('home'))
    return render_template("add_user.html")

#update user using ID
@app.route('/update/<string:id>',methods=['GET','POST'])
def update(id):
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        city=request.form['city']
        res=con.cursor(dictionary=True)
        sql="update users set name=%s,age=%s,city=%s where id=%s"
        value=(name,age,city,id)
        res.execute(sql,value)
        con.commit()
        flash("Update user")
        return redirect(url_for("home"))
    res=con.cursor(dictionary=True)
    sql="select * from users where id=%s"
    value=(id,)
    res.execute(sql,value)
    result=res.fetchone()
    return render_template("update.html",datas=result)

@app.route('/delete/<string:id>',methods=['GET','POST'])
def delete(id):
        res=con.cursor(dictionary=True)
        sql="delete from users where id=%s"
        value=(id,)
        res.execute(sql,value)
        con.commit()
        flash("User deleted")
        return redirect(url_for('home'))


if (__name__=="__main__"):
    app.secret_key = "ajith123"
    app.run(debug=True)