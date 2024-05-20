#!/usr/bin/python3
'''
This script retrieves the TODO list progress of every employee
and exports this information to a JSON file. It uses the JSONPlaceholder API to
fetch the necessary information.

The script outputs a JSON file named `todo_all_employees.json` containing the
tasks of all employees with details on their completion status.
'''

# Import the json module to handle JSON file operations
import json

# Import the requests library to handle HTTP requests
import requests

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API to fetch all users
    base_url = 'https://jsonplaceholder.typicode.com/users/'

    # Make a GET request to fetch all users
    users_response = requests.get(base_url)
    users = users_response.json()

    # Initialize an empty dictionary to hold the data for all employees
    all_employees_data = {}

    # Loop through each user to fetch their TODO list
    for user in users:
        user_id = user['id']
        username = user['username']

        # Make a GET request to fetch the user's TODO list
        todos_url = '{}{}/todos'.format(base_url, user_id)
        todos_response = requests.get(todos_url)
        todos_list = todos_response.json()

        # Initialize a list to hold the tasks for the current user
        user_tasks = []

        # Populate the list with task details
        for task in todos_list:
            task_data = {
                "task": task["title"],
                "completed": task["completed"],
                "username": username
            }
            user_tasks.append(task_data)

        # Add the user's tasks to the main dictionary
        all_employees_data[user_id] = user_tasks

    # Write the data to a JSON file named 'todo_all_employees.json'
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_employees_data, json_file)
