from flask import Flask, render_template, redirect
app=Flask(__name__)
@app.route('/')
@app.route('/prediction_page_1')
def prediction_page_1():
    return render_template('webpage1.html')
@app.route('/registration-page')
def registration_page():
    return redirect(url_for('webpage3.html'))