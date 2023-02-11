#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees to 
be exported to csv"""

import csv
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId
    file_name = '{}.csv'.format(employeeId)

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

#    csv_file = open('USER_ID.csv', 'w')
#    csv_writer = csv.writer(csv_file)

#    for task in tasks:
#        row = []
#        row.append(employeeId)
#        row.append(employeeName)
#        row.append(task.get('completed'))
#        row.append(task.get('title'))
#        csv_writer.writerow(row)

#    csv_file.close()

with open(file_name, 'w') as fd:
    for task in tasks:
        fd.write('"{}","{}","{}","{}"\n'
                 .format(employeeId, employeeName,
                         task.get('completed'), task.get('title')))
