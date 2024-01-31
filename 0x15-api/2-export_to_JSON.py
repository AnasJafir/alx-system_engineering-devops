#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    if user.status_code != 200:
        print("Error: User not found")
        sys.exit(1)

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    if todos.status_code != 200:
        print("Error: Unable to fetch TODO data")
        sys.exit(1)

    todos = todos.json()

    todoUser = {}
    taskList = []

    for task in todos:
        if task.get('userId') == int(userId):
            taskDict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user.json().get('username')
            }
            taskList.append(taskDict)

    todoUser[userId] = taskList

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
