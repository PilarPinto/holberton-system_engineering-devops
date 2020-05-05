#!/usr/bin/python3
'''
Gatherin data form REST API dummy JSON file
and made a export JSON format with format
'''
import json
import requests
import sys

if __name__ == "__main__":

    employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/').json()
    num_task = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()

    json_name = 'todo_all_employees'
    employees = {}
    wrap_dict = {}

    with open('{}.json'.format(json_name), 'w') as f:
        for i in employee:
            employee_id = i.get('id')
            wrap_dict[employee_id] = []
            employees[employee_id] = i.get('username')

        for ind in num_task:
            inner_dict = {}
            employee_id = ind.get('userId')
            inner_dict['task'] = ind.get('title')
            inner_dict['completed'] = ind.get('completed')
            inner_dict['username'] = employees.get(employee_id)
            wrap_dict.get(employee_id).append(inner_dict)
        json.dump(wrap_dict, f)
