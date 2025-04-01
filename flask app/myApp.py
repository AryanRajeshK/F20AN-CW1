from flask import Flask, render_template, url_for, redirect, flash, session
from forms import userLoginForm
import os
from flask_sqlalchemy import SQLAlchemy
# from models import User
import sqlite3

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
dbPath = os.path.join(basedir, 'database.sqlite3')


########## For setting up the app environment ###########

# setting up SQlAlchemy only for easy setupDatabase.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite3')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  
db = SQLAlchemy(app)
# csrf security
app.config['SECRET_KEY'] = 'topSecretKey'

# model
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password



########## functions ##########
# connecting to local server
def getDbConnection():
    connection = sqlite3.connect(dbPath)
    connection.row_factory = sqlite3.Row
    return connection




########### views ###########

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = userLoginForm()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        # reset the form fields
        form.username.data = ''
        form.password.data=''
        
        connection = getDbConnection()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        user = ''
        try:
            user = connection.execute(query).fetchone()
        except Exception as e:
            flash(f'Error encountered: {str(e)}')
            print(f"Error: {e}")
        connection.close()
        
        if user:
            session['username'] = user['username']
            flash(f"Welcome {user['username']}!", "success")
            return redirect(url_for('admin')) if session['username'] == "admin" else redirect(url_for('index'))
        
        else:
            flash(f'Invalid username or password! Try Again.')
    
    
    
    return render_template('login.html', form = form)
    

@app.route('/admin')
def admin():
    if 'username' in session and session['username'] == "admin":
        return render_template("admin.html") 
    else:
        flash("Unauthorized access to admin prevented!")
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove 'username' from the session
    flash("You have been logged out.")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)