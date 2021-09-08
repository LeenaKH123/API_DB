'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests
import json
NewUser = {'first_name': 'Leena2', 'last_name': 'K2', 'email': 'engleena2@outlook.com'}
url = 'http://demo.codingnomads.co:8080/tasks_api/users'
x = requests.put(url, json=NewUser)
print(x.status_code, x.reason)
response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")
output = (response.json())
output1 = output["data"]
print(output1)