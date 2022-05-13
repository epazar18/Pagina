
from socket import SocketIO
from flask import Flask, render_template, request,redirect, url_for, session 
from flask_login import LoginManager

app= Flask(__name__)


@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/login')
def login():
  
        return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')
     
@app.route('/principal')
def home1():
    return render_template('home.html')


if __name__=="__main__":
    app.run(debug=True)

