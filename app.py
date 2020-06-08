from flask import Flask, render_template, jsonify, redirect, url_for, request
# from scrape import scrape
from dao.database import getLatest, getRangeDowData, getMonthlyDeathsData
from load_data import load
from fredapi import Fred

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
    deathData = getMonthlyDeathsData()
    del deathData[-1]
    jsonDeathData = str(JSONEncoder().encode(deathData))
    return render_template('dashboard.html', jsonDeathData = jsonDeathData)

@app.route('/template_data')
def template_data():
    data = getLatest()
    return render_template('template_data.html', data = data)

@app.route('/spanish_flu')
def spanish_flu():
    spanish_flu_data = getRangeDowData(1917,1922)
    json_spanish_flu_data = str(JSONEncoder().encode(spanish_flu_data))
    return render_template('spanish_flu.html', data = json_spanish_flu_data)

@app.route('/asian_flu')
def asian_flu():
    data = getLatest()
    return render_template('asian_flu.html', data = data)
@app.route('/conclusions')
def conclusions():
    
    return render_template('conclusions.html')

@app.route('/hong_kong_flu')
def hong_kong_flu():
    hong_kong_data = getRangeDowData(1968,1973)
    hong_kong_data1=getMonthlyDeathsData()
    json_hong_kong_data1 = str(JSONEncoder().encode(hong_kong_data1))
    json_hong_kong_data = str(JSONEncoder().encode(hong_kong_data))
    return render_template('hong_kong_flu.html', data1 = json_hong_kong_data,data2=json_hong_kong_data1)


@app.route('/swine_flu')
def swine_flu():
    newData = getRangeDowData(2009,2015)
    jsonNewData4 = str(JSONEncoder().encode(newData))
    #print("swine flue data ")
    print(jsonNewData4)
    return render_template('swine_flu.html', data = jsonNewData4)

@app.route('/combined_data')
def combined_data():
    newData = getRangeDowData(1957,1960)
    jsonNewData5 = str(JSONEncoder().encode(newData))
    #print("swine flue data ")
    #print(jsonNewData4)
    return render_template('combined_data.html', data = jsonNewData5)   

@app.route('/coronavirus')
def coronavirus():
    my_key = "5d898dd8f945e9190745a8e4f666f64c"
    fred = Fred(api_key=my_key)
    import pandas as pd
    goldData = fred.get_series_latest_release('GOLDAMGBD228NLBM')
    dowData = fred.get_series_latest_release('DJIA')
    result = pd.concat([goldData, dowData], axis=1, sort=False)
    dgdata = result.apply (pd.to_numeric, errors='coerce')
    df = dgdata.dropna(how='any',axis=0) 
    df['dowoverGold'] = df[1] / df[0]
    resultdata = df.tail(90)
    resultdata = resultdata.round(2)
    resultdata.drop(resultdata.columns[0], axis=1, inplace=True)
    resultdata.drop(resultdata.columns[0], axis=1, inplace=True)
    #resultdata.index.name = 'date'
    resultdata['date'] = resultdata.index
    resultdata['date'] = resultdata['date'].astype(str)
    rdata = resultdata.to_json(orient='records')
    #resultresultdata.itterrows()
    print(rdata)
    return render_template('coronavirus.html', data = rdata)

# run the app
if __name__ == '__main__':
    app.run(debug=True)