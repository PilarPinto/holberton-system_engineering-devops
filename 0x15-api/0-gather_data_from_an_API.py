#!/usr/bin/python3
'''
Gatherin data form REST API dummy JSON file
'''
import requests
import sys

if __name__ == "__main__":

    employee_id = sys.argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(employee_id)).json()
    num_task = requests.get('https://jsonplaceholder.typicode.com/todos',
                            params={'userId': employee_id}).json()

    employee_name = employee.get('name')
    tasks = []
    total_number_tasks = 0
    number_done_task = 0
    for ind in num_task:
        total_number_tasks += 1
        if ind.get('completed'):
            tasks.append(ind.get('title'))
            number_done_task += 1

    print('Employee {} is done with tasks({}/{})'.format(
        employee_name, number_done_task, total_number_tasks))

    for phrase in tasks:
        print('\t', phrase)
