import json
import requests
import pandas as pd
import mysql.connector as mysql
from pandas.io import sql

from bs4 import BeautifulSoup
# Collect first page of artists’ list
page = requests.get('https://www.forbes.com/ajax/list/data?year=2018&uri=global2000&type=organization')
print(page.json())

data = page.json()
#name = data[0]['name']
#print(data)
#df = pd.DataFrame(data, columns=["position","rank","name","uri","imageUri","industry","country","revenue","marketValue","headquarters","ceo","profits","assets"])
#print(df)

print("starting dbwork")
db = mysql.connect(
  host="localhost",
  user="root",
  passwd="admin123",
  database='my_db',

)




cursor = db.cursor()
print("starting truncation")
cursor.execute("TRUNCATE TABLE forbes_2000_landing;")

print("starting insert")
for transaction in data:
    if 'industry' in transaction:
        transaction_sql = (
        """insert into forbes_2000_landing
        (position, rank, name, uri, imageUri, industry, country)
        values (%(position)s, %(rank)s, %(name)s, %(uri)s, %(imageUri)s,  %(industry)s , %(country)s )"""
        #   %(revenue)s, %(marketValue)s, %(headquarters)s, %(ceo)s, %(profits)d, %(assets)s)

         )
    else:
            transaction_sql = (
            """insert into forbes_2000_landing
            (position, rank, name, uri, imageUri,  country)
            values (%(position)s, %(rank)s, %(name)s, %(uri)s, %(imageUri)s,  %(country)s )"""
            #   %(revenue)s, %(marketValue)s, %(headquarters)s, %(ceo)s, %(profits)d, %(assets)s)

        )
    print(transaction_sql)
    print(transaction)
    cursor.execute(transaction_sql, transaction)

db.commit()

cursor.close()