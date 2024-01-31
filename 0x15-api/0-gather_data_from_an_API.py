#!/usr/bin/python3
"""For a given employee ID, returns information about
their todo list progress"""

import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))

    if user.status_code != 200:
        print("Error: User not found")
        sys.exit(1)

    name = user.json().get('name')

    todo = requests.get('https://jsonplaceholder.typicode.com/todos')

    if todo.status_code != 200:
        print("Error: Unable to fetch TODO data")
        sys.exit(1)

    total = 0
    done = 0

    for task in todo.json():
        if task.get('userId') == int(user_id):
            total += 1
            if task.get('completed'):
                done += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, done, total))

    print('\n'.join(["\t " + task.get('title') for task in todo.json()
          if task.get('userId') == int(user_id) and task.get('completed')]))
