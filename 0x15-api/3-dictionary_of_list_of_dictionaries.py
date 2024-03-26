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
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'

    user = get(url_user + str(emp_id)).json().get('username')

    params = {'userId': emp_id}
    tasks = get(url_todo, params=params).json()
    task_list = []
    for task in tasks:
        task_list.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user})
    return({emp_id: task_list})


def get_all_emp():
    """Method that returns list of dictionnaries of all task of all users"""
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    file_name_users = "todo_all_employees.json"
    users = get(url_user).json()
    to_do_list = {}
    for user in users:
        to_do_list.update(todo_to_json(user.get('id')))
    with open(file_name_users, 'w') as f:
        dump(to_do_list, f)


if __name__ == '__main__':
    get_all_emp()
