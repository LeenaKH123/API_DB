# Using the API from the API section, write a program that makes a request to
# get all of the users and all of their tasks.
# Create tables in a new local database to model this data.
# Think about what tables are required to model this data. Do you need two tables? Three?
# Persist the data returned from the API to your database.
# NOTE: If you run this several times you will be saving the same information in the table.
# To prevent this, you should add a check to see if the record already exists before inserting it.
import requests
import json
import sqlalchemy

engine = sqlalchemy.create_engine(
    "mysql+pymysql://leena:leena@localhost/CustomersTasks"
)
connection = engine.connect()
metadata = sqlalchemy.MetaData()
newTable = sqlalchemy.Table("UsersTasks", metadata, autoload=True, autoload_with=engine)
# getting all the userscd
url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(url)
output = response.json()
outputData = output["data"]
# print(outputData) -- it works
# getting all the users ID's
userid = []
for item in outputData:
    userid.append(item["id"])
# print(userid)clear
# getting all tasks
users = []
tasks = []
for id in userid:
    responsetask = requests.get(url + "/" + str(id) + "/tasks")
    outputtasks = responsetask.json()
    outputtaskdata = outputtasks["data"]
    for item2 in outputtaskdata:
        users.append(item2["name"])
        tasks.append(item2["description"])
    # print(outputtaskdata)
# print("users", users)  -- 59
# print("tasks", tasks)  -- 59
# print("id's", userid)  -- 200's
# urlTask =
# insert list elements in the database
for index in range(len(users)):

    query = sqlalchemy.insert(newTable).values(
        Name=users[index], Desctiption=tasks[index], Identifier=userid[index]
    )
    result_proxy = connection.execute(query)
print("The database was successfully updated")
