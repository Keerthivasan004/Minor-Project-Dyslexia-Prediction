from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
@app.route('/prediction_page_1')
def prediction_page_1():
    return render_template('webpage1.html')
@app.route('/prediction_page_2')
def prediction_page_2():
    return render_template('webpage2.html')
@app.route('/prediction_page_4')
def prediction_page_4():
    return render_template('webpage4.html')
if __name__==("__main__"):
    app.run(debug=True)