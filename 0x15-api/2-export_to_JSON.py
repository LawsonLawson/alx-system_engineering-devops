#!/usr/bin/python3
'''
This script retrieves the TODO list progress of a given employee by their ID
and exports this information to a JSON file. It uses the JSONPlaceholder API to
fetch the necessary information.

The script outputs a JSON file named with the employee's ID containing the
employee's tasks with details on their completion status.
'''

# Import the json module to handle JSON file operations
import json

# Import the requests library to handle HTTP requests
import requests

# Import argv from sys to handle command-line arguments
from sys import argv

if __name__ == "__main__":
    # Check if the script receives the correct number of arguments
    if len(argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        exit(1)

    # Construct URL to fetch user information based on the provided employee ID
    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    # Make a GET request to the API to retrieve user information
    user_response = requests.get(user_url)

    # Check if the user exists
    if user_response.status_code != 200:
        print("User ID not found")
        exit(1)

    # Extract the username of the user from the JSON response
    user_data = user_response.json()
    username = user_data.get("username")

    # Make another GET request to retrieve the user's TODO list
    todos_url = '{}/todos'.format(user_url)
    todos_response = requests.get(todos_url)
    todos_list = todos_response.json()

    # Prepare the data structure to hold the tasks
    tasks_data = {user_id: []}

    # Iterate through the list of tasks and populate the data structure
    for task in todos_list:
        task_completed = task["completed"]
        task_title = task["title"]
        tasks_data[user_id].append({
            "task": task_title,
            "completed": task_completed,
            "username": username
        })

    # Write the tasks data to a JSON file named with the employee ID
    json_filename = '{}.json'.format(user_id)
    with open(json_filename, 'w') as json_file:
        json.dump(tasks_data, json_file)
