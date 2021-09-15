"""

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
"""
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
    print("I dont know what to do here")

elif selection == "4":
    print("I dont know what to do here")


# elif selection == '3':

# elif selection == '4':

# elif selection == '5':

# elif selection == '6':

# elif selection == '7':
