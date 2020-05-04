#!/usr/bin/python3
'''
Gatherin data form REST API dummy JSON file
and export to JSON
'''
import json
import requests
import sys

if __name__ == "__main__":

    employee_id = sys.argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(employee_id)).json()
    num_task = requests.get('https://jsonplaceholder.typicode.com/todos',
                            params={'userId': employee_id}).json()
    tasks = []
    wrap_dict = {}
    with open('{}.json'.format(employee_id), 'w', newline='') as f:
        for ind in num_task:
            inner_dict = {}
            inner_dict['task'] = ind.get('title')
            inner_dict['completed'] = ind.get('completed')
            inner_dict['username'] = employee.get('username')
            tasks.append(inner_dict)
        wrap_dict[employee_id] = tasks
        json.dump(wrap_dict, f)
