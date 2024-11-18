from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
@app.route('/prediction-page-1')
def prediction_page_1():
    return render_template('webpage1.html')