<<<<<<< HEAD
'''
=======
"""

>>>>>>> 7856ef653394a526e65c67837963d4168e968336
Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:
Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)
It is your responsibility to build out the application to handle all menu options above.
<<<<<<< HEAD
'''
=======
"""
>>>>>>> 7856ef653394a526e65c67837963d4168e968336
import requests
import json

url = "http://demo.codingnomads.co:8080/tasks_api/users"
selection = input(
    "Please select from the following options (enter the number of the action you would like to take) \n 1) create a new account \n 2) View all your tasks \n 3) View your completed tasks \n 4) View only your incomplete tasks \n 5) Create a new task \n 6) Update an existing task \n 7) Delete a task \n"
)
if selection == "1":
    print("We will create a new account for you ")
    firstName = input("Type your First Name ")
    lastName = input("Type your Last Name ")
    email = input("Type in your email ")
    NewUser = {"first_name": firstName, "last_name": lastName, "email": email}
    x = requests.post(url, json=NewUser)

elif selection == "2":
    userid = input("Please type your userid to show all your tasks ")
    response = requests.get(url + "/" + userid + "/" + "tasks?complete=-1")
    output = response.json()
    outputData = output["data"]

    for item in outputData:
        print(item)
        if item["userId"] == userid:
            print(item)
        # else:
        #     print("Your ID doesn't exist")

elif selection == "3":
    userid = input("Please type your userid to show all your completed tasks ")
    response = requests.get(url + "/" + userid + "/" + "tasks?complete=true")
    output = response.json()
    outputData = output["data"]

    for item in outputData:
        print(item)
        if item["userId"] == userid:
            print(item)

elif selection == "4":
    userid = input("Please type your userid to show all your incompleted tasks ")
    response = requests.get(url + "/" + userid + "/" + "tasks?complete=false")
    output = response.json()
    outputData = output["data"]

    for item in outputData:
        print(item)
        if item["userId"] == userid:
            print(item)

elif selection == "5":
    print("We will create a new task for you ")
    description = input("Type your task description ")
    taskName = input("Type your Name ")
    taskuserid = input("Type a task user ID ")
    NewUser = {"description": description, "name": taskName, "userId": taskuserid}
    taskurl = "http://demo.codingnomads.co:8080/tasks_api/tasks"
    x = requests.post(taskurl, json=NewUser)
    print(x.status_code)

elif selection == "6":
    print("We will update a task for you ")
    taskurl = "http://demo.codingnomads.co:8080/tasks_api/tasks"
    description = input("Type your task description ")
    taskName = input("Type your Name ")
    taskuserid = input("Type a task user ID ")
    NewUser = {"description": description, "name": taskName, "userId": taskuserid}
    x = requests.post(taskurl, json=NewUser)
    print(x.status_code)

elif selection == "7":
    idDelete = input("Please type the ID for the task you want to delete ")
    taskurl = "http://demo.codingnomads.co:8080/tasks_api/tasks"
    response = requests.delete(taskurl + "/" + idDelete)
    print(response.status_code)


#     A few thoughts:
# I'd recommend splitting off the work into individual functions.
# That way you have a nice re-usable codebase with simple functions you can call to invoke the 
# behavior for each selection
# In the selection == "2" option - you do not need to include ?complete=-1  
# - the default behavior will return all tasks complete or incomplete.
#  If you want only completed tasks then you'd add ?complete=true 
#  - for instance http://demo.codingnomads.co:8080/tasks_api/users/3/tasks?complete=true or inversely,
#   http://demo.codingnomads.co:8080/tasks_api/users/3/tasks?complete=false
# in various sections you're checking if item["userId"] == userid - 
# I'm not sure this is necessary as you've specifically queries the REST API using 
# that specific userId which will only return elements and data for that user - so that check seems redundant
