#!/usr/bin/python3
""" Script to get TODO list progress
    by employee ID and save it to
    JSON file
"""
from json import dump
from requests import get
from sys import argv


def todo_to_json(emp_id):
    """ Send request for employee's
        to do list to API
    """
    file_name = '{}.json'.format(emp_id)
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'

    # check if user exists
    user = get(url_user + emp_id).json().get('username')

    if user:
        params = {'userId': emp_id}
        #  get all tasks
        tasks = get(url_todo, params=params).json()
        task_list = []
        for task in tasks:
            task_list.append({"task": task.get('title'),
                              "completed": task.get('completed'),
                              "username": user})
        with open(file_name, 'w') as f:
            dump({emp_id: task_list}, f)


if __name__ == '__main__':
    if len(argv) > 1:
        todo_to_json(argv[1])
