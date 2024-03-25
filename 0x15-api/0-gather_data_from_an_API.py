#!/usr/bin/python3
"""Module to gather data from api"""
import requests
import sys


def get_employee_todo_list_progress(employee_id):
    """Method to gather data from api"""
    employee_infos = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                employee_id
                )
            ).json()
    todo_list = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                employee_id
                )
            ).json()
    employee_name = employee_infos['name']
    total_todos = len(todo_list)
    completed_tasks = []
    for todo in todo_list:
        if todo['completed']:
            completed_tasks.append(todo['title'])
    num_completed_tasks = len(completed_tasks)
    print('Employee {} is done with tasks({}/{}):'.format(
        employee_name, num_completed_tasks, total_todos
        ))
    for task_title in completed_tasks:
        print('\t{}'.format(task_title))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_list_progress(employee_id)
