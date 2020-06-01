
from flask import Flask, render_template, jsonify, redirect, url_for, request
# from scrape import scrape
from dao.database import getLatest,  getRangeDowData, getMonthlyDeathsData
from load_data import load

import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)



load()

#print(newData)

# Create an instance of our Flask app.
app = Flask(__name__, static_url_path='')

# update()
# index
@app.route('/', methods=['GET', 'POST'])
def index():
    # call to database to get latest data
    yearData = getRangeDowData(1918,1920)
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

@app.route('/spanish_flu_1918')
def spanish_flu():
    spanish_flu_data = getRangeDowData(1918,1919)
    json_spanish_flu_data = str(JSONEncoder().encode(spanish_flu_data))
    return render_template('spanish_flu.html', data = json_spanish_flu_data)

@app.route('/asian_flu')
def asian_flu():
    data = getLatest()
    return render_template('asian_flu.html', data = data)

@app.route('/hong_kong_flu')
def hong_kong_flu():
    newData = getRangeDowData(1968,1973)
    jsonNewData3 = str(JSONEncoder().encode(newData))
    return render_template('hong_kong_flu.html', data = jsonNewData3)

@app.route('/swine_flu')
def swine_flu():
    data = getLatest()
    return render_template('swine_flu.html', data = data)

@app.route('/coronavirus')
def coronavirus():
    data = getLatest()
    return render_template('coronavirus.html', data = data)




''' test route that renders data from mongo into a plotly graph 
you can select the years for your pandemic in getRangeDowData
'''

@app.route('/render_test')
def renderTest():
    newData = getRangeDowData(1918,1920)

    jsonNewData2 = str(JSONEncoder().encode(newData))
    #print(jsonNewData2)

    deathData = getMonthlyDeathsData()
    jsonNewData3 = str(JSONEncoder().encode(deathData))

    return render_template('render_test.html', data = jsonNewData2, deathData = jsonNewData3)
    


# run the app
if __name__ == '__main__':
    app.run(debug=True)