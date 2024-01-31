#!/usr/bin/python3
"""For a given employee ID, returns information about
their todo list progress"""

import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))

    name = user.json().get('name')

    todo = requests.get('https://jsonplaceholder.typicode.com/todo')
    total = 0
    done = 0

    for task in todo.json():
        if task.get('user_id') == int(user_id):
            total += 1
            if task.get('done'):
                done += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, done, total))

    print('\n'.join(["\t " + task.get('title') for task in todo.json()
          if task.get('user_id') == int(user_id) and task.get('done')]))
