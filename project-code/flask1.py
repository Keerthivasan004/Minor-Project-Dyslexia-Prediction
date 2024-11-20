from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
@app.route('/prediction_page_1')
def prediction_page_1():
    return render_template('webpage1.html')
@app.route('/prediction_page_2')
def prediction_page_2():
    return render_template('webpage3.html')