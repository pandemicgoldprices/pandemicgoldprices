
from flask import Flask, render_template, jsonify

# from scrape import scrape

from dao.database import getLatest

from load_data import load

load()



# Create an instance of our Flask app.
app = Flask(__name__)

#update()
#index
# added comment to sean branchgi
@app.route('/')
def index():
    # call to database to get latest data
    data = getLatest()
    return render_template('index.html', data = data )

@app.route('/update')
def updateMe():

    # call to database.py to update data
    #update()

    return index()

@app.route('/intro')
def intro():
    data = getLatest()
    return render_template('intro.html', data = data)

@app.route('/dashboard')
def dashboard():
    data = getLatest()
    return render_template('dashboard.html', data = data)

@app.route('/templatedata')
def templatedata():
    data = getLatest()
    return render_template('templatedata.html', data = data)

#run the app
if __name__ == '__main__':
#=======
# from flask import Flask, render_template, jsonify

# from scrape import scrape

# from dao.database import getLatest, update



# # Create an instance of our Flask app.
# app = Flask(__name__)

# #update()
# #index
# @app.route('/')
# def index():
#     # call to database to get latest data
#     data = getLatest()
#     return render_template('index.html', data = data )

# @app.route('/update')
# def updateMe():

#     # call to database.py to update data
#     update()

#     return index()

# #run the app
# if __name__ == '__main__':

    app.run(debug=True)