'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''
import requests
import json
NewUser = {'id': 100, 'first_name': 'Leena', 'last_name': 'K', 'email': 'engleena@outlook.com'}
url = 'http://demo.codingnomads.co:8080/tasks_api/users'
x = requests.post(url, json= NewUser)
print(x.status_code, x.reason)
response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")
output = (response.json())
output1 = output["data"]
print(output1)
