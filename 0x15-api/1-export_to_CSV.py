#!/usr/bin/python3
'''
Gatherin data form REST API dummy JSON file
and export depending a user_id to a csv file
'''
import csv
import requests
import sys

if __name__ == "__main__":

    employee_id = sys.argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(employee_id)).json()
    num_task = requests.get('https://jsonplaceholder.typicode.com/todos',
                            params={'userId': employee_id}).json()

    employee_name = employee.get('name')

    with open('{}.csv'.format(employee_id), 'w', newline='') as f:
        writer2csv = csv.writer(f, quoting=csv.QUOTE_ALL)
        for ind in num_task:
            writer2csv.writerow([employee_id, employee.get(
                'username'), ind.get('completed'), ind.get('title')])
