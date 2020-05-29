import pymongo

# in pycharm if there is a red line under the package mongo if you move your mouse over it then it will ask to install
# click install and pycharm will do the pip for you

# random number library in python
import random

'''
to install mongodb on OSX
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
You need to install with brew and then start the mongo server
once you run the server type mongo in terminal to check if it's working
you can close the terminal after starting mongo it will keep running
'''

'''
FUNCTION WHICH CONNECTS TO THE MONGO DB VIA PYMONGO AND GET"S THE LATEST ENTRY
'''
def getLatest():
    # Create connection variable
    conn = 'mongodb://localhost:27017'

    # Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

    # Connect to a database. Will create one if not already available.
    # thid creates a schema called etlProject

    db = client.myDB.dowGoldHistory

    # query the DB
    dataOut = db.find().sort('_id', -1)
    # count the records
    results_count = str(dataOut.count())
    print("results count :" + results_count)
    # display top record
    print(dataOut[0])

def getDataDateRange(begin, end):
    data = {}
    return data
