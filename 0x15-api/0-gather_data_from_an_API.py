#!/usr/bin/python3
'''
This script retrieves and displays the TODO list progress of a given employee
by their ID. It uses the JSONPlaceholder API to fetch the necessary information

The script prints the employee's name, the number of completed tasks, and the
total number of tasks. It also lists the titles of the completed tasks.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
'''

# Import the requests library to handle HTTP requests
import requests

# Import argv from sys to handle command-line arguments
from sys import argv

if __name__ == "__main__":
    # Check if the script receives the correct number of arguments
    if len(argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
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

    # Extract the name of the user from the JSON response
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Make another GET request to retrieve the user's TODO list
    todos_url = '{}/todos'.format(user_url)
    todos_response = requests.get(todos_url)
    todos_list = todos_response.json()

    # Total number of tasks
    total_tasks = len(todos_list)

    # Make a GET request to retrieve only the completed tasks
    completed_tasks_response = requests.get(todos_url,
                                            params={"completed": "true"})
    completed_tasks_list = completed_tasks_response.json()

    # Number of completed tasks
    completed_tasks_count = len(completed_tasks_list)

    # Print the employee's name, and the count of completed and total tasks
    print("Employee {} is done with tasks({}/{}):".format
          (employee_name, completed_tasks_count, total_tasks))

    # Iterate through the list of completed tasks and print their titles
    for task in completed_tasks_list:
        print("\t {}".format(task["title"]))
