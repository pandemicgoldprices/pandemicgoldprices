
# import what we need
import pymongo
import pandas as pd
import numpy as np
import datetime as datetime
#import matplotlib.pyplot as pltconda
#import plotly.graph_objects as go

# function which collects data from CSV files and dumps into mongo DB database
def load():

    GOLD_df = pd.read_csv('data/GOLD_monthly_cleaned.csv', encoding='utf-8', delimiter=',', engine='python')
    DJIA_df = pd.read_csv('data/DJIA_monthly_cleaned.csv', encoding='utf-8', delimiter=',', engine='python')


    DJIA_df.rename(columns={"yearmonth_str": "date"})


    COMBINED_df = pd.merge(GOLD_df, DJIA_df)

    COMBINED_df = COMBINED_df.rename(columns={'nominal_price_USD': 'gold_nominal_price_USD'})

    print(COMBINED_df)
    conn = 'mongodb://localhost:27017'

        # Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

        # Connect to a database. Will create one if not already available.

    db = client.myDB.dowGoldHistory
    # clear the DB
    db.drop()
    # recreate it
    db = client.myDB.dowGoldHistory
    # convert pandas DF to dict
    data = COMBINED_df.to_dict(orient='records')  # Here's our added param..
    # dump it it
    db.insert_many(data)
    # query the DB
    dataOut = db.find().sort('_id', -1)
    # count the records
    results_count = str(dataOut.count())
    print("results count :" + results_count)
    # display top record
    print(dataOut[0])
