#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    # Get user ID from command line arguments
    userid = sys.argv[1]

    # Fetch user data from API
    user = '{}users/{}'.format(url, userid)
    res = requests.get(user)
    json_o = res.json()
    username = json_o.get('username')  # Store username

    # Fetch todos for user from API
    todos = '{}todos?userId={}'.format(url, userid)
    res = requests.get(todos)
    tasks = res.json()

    # For each todo, store relevant data in l_task
    l_task = []
    for task in tasks:
        l_task.append({"task": task.get('title'),
                       "completed": task.get('completed'),
                       "username": username})

    # Write data to JSON file
    filename = '{}.json'.format(userid)
    with open(filename, mode='w') as employee_file:
        json.dump({userid: l_task}, employee_file)  # Write the dictionary to a JSON file
