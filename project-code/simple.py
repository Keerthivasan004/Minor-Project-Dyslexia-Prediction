from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return "Hello World"
@app.route('/user/<users>')
def user(users):
    return f'<h1>Hello from {users}</h1>'