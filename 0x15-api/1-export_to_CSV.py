#!/usr/bin/python3
'''
This script retrieves the TODO list progress of a given employee by their ID
and exports this information to a CSV file. It uses the JSONPlaceholder API to
fetch the necessary information.

The script outputs a CSV file named with the employee's ID containing the
employee's tasks with details on their completion status.
'''

# Import the csv module to handle CSV file operations
import csv

# Import the requests library to handle HTTP requests
import requests

# Import argv from sys to handle command-line arguments
from sys import argv

if __name__ == "__main__":
    # Check if the script receives the correct number of arguments
    if len(argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
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

    # Open a CSV file for writing, named with the employee ID
    csv_filename = '{}.csv'.format(user_id)
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)

        # Write each task's details to the CSV file
        for task in todos_list:
            task_completed = task["completed"]
            task_title = task["title"]
            csv_writer.writerow([user_id, username, task_completed,
                                task_title])
