#!/usr/bin/python3
"""Module to export gathered data to csv format"""
import requests
import sys


def get_employee_todo_list_progress(employee_id):
    """Method to export gathered data to csv format"""
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
    with open('{}.csv'.format(employee_id), 'w') as f:
        for task in todo_list:
            f.write('"{}","{}","{}","{}"\n'
                    .format(
                        employee_id, employee_infos[
                            'username'
                            ], task[
                                'completed'
                                ], task[
                                    'title'
                                    ]
                        ))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_list_progress(employee_id)
