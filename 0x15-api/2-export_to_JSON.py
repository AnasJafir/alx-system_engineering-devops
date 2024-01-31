#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todoUser = {}
    taskList = []

    for task in todos:
        if task.get('user_id') == int(user_id):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)
    todoUser[user_id] = taskList

    filename = user_id + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
