
from flask import Flask, render_template, jsonify
# from scrape import scrape
from dao.database import getLatest
from load_data import load

load()

# Create an instance of our Flask app.
app = Flask(__name__)

# update()
# index
@app.route('/')
def index():
    # call to database to get latest data
    data = getLatest()
    return render_template('index.html', data = data )

@app.route('/update')
def updateMe():
    # call to database.py to update data
    # update()
    return index()

@app.route('/introduction')
def introduction():
    data = getLatest()
    return render_template('introduction.html', data = data)

@app.route('/dashboard')
def dashboard():
    data = getLatest()
    return render_template('dashboard.html', data = data)

@app.route('/template_data')
def template_data():
    data = getLatest()
    return render_template('template_data.html', data = data)

@app.route('/spanish_flu')
def spanish_flu():
    data = getLatest()
    return render_template('spanish_flu.html', data = data)

@app.route('/asian_flu')
def asian_flu():
    data = getLatest()
    return render_template('asian_flu.html', data = data)

@app.route('/hong_kong_flu')
def hong_kong_flu():
    data = getLatest()
    return render_template('hong_kong_flu.html', data = data)

@app.route('/swine_flu')
def swine_flu():
    data = getLatest()
    return render_template('swine_flu.html', data = data)

@app.route('/coronavirus')
def coronavirus():
    data = getLatest()
    return render_template('coronavirus.html', data = data)

# run the app
if __name__ == '__main__':
    app.run(debug=True)