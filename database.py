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
    db = client.etlProject

    # get the record that was inserted last
    data = db.myDB.find().sort('_id', -1)
    print(data[0])
    return data[0]

'''
FUNCTION WHICH CRETES SOME RANDOM DATA AND STORES IN THE DB
'''
def update():
    # Create connection variable
    conn = 'mongodb://localhost:27017'

    # Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

    # Connect to a database. Will create one if not already available.
    db = client.etlProject
    # generate two random numbers
    randomInt = random.randint(1,10001)
    randomintTwo = random.randint(1,100001)

    #create some data
    myData = {"key": randomintTwo, "value" : randomInt }

    # insert mData into DB
    data = db.myDB
    post_id = data.insert_one(myData).inserted_id
    print(post_id)

#run this to test an insertion of data
update()
#run this to get the latest entry into the DB
getLatest()