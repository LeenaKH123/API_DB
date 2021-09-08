"""
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

"""
import requests
import json
import re
regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")
output = (response.json())
output1 = output["data"]
# print(type(output))
# print(output1)
for email in output1:
    print(output1('email'))