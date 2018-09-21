import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="root",
  passwd="admin123",
database='my_db'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM t2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

cursor = db.cursor()

cursor.execute("TRUNCATE TABLE forbes_2000_landing;")
db.commit()

transaction_sql = (
  "insert into forbes_2000_landing"
  "(position, rank, name, uri, imageUri, industry, country, revenue, marketValue, headquarters, ceo, profits, assets)"
  "values (%(position)s, %( rank)s, %( name)s, %( uri)s, %( imageUri)s, %( industry)s, %( country)s, %( revenue)s, %( marketValue)s, %( headquarters)s, %( ceo)s, %( profits)s, %( assets)s")

for transaction in data:
  cursor.execute(transaction_sql, transaction)

# this for loop I want change and try with lambda and map expression like this
## (it works without errors but not load data. Why? What is wrong?
# map(lambda transaction: cursor.execute(transaction_sql, transaction), json_list_of_transactions )

db.commit()

cursor.close()
db.close()