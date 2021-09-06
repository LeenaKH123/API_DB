"""
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

"""
import requests
import re

regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")
print(response.status_code)
print(response.encoding)
# print(response.content)
# print(response.json())
users = []
for email in response.content:
    if re.search(regex, email):
        print(email)
