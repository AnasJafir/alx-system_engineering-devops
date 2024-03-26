#!/usr/bin/python3
"""Module to export gathered data to csv format"""
import requests
import sys


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)
    username = response.json().get('username')

    todos = url + "/todos"
    response = requests.get(todos)
    tasks = response.json()

    with open('{}.csv'.format(employee_id), 'w') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'
                    .format(
                        employee_id, username, task.get(
                            'completed'
                            ), task.get('title')))
