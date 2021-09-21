'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''
import requests
import json

# getting all the users
url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(url)
output = response.json()
outputData = output["data"]
# print(outputData) -- it works

# getting all the users ID's
userid = []
for item in outputData:
    userid.append(item["id"])
#print(userid) 

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
print("users", users)
print("tasks", tasks)
#urlTask = 