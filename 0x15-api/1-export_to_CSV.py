#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys
import csv

if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
#    done = 0
#    done_tasks = []

#    print ('response (tasks):', tasks)
#    for task in tasks:
#        if task.get('completed'):
#            done_tasks.append(task)
#            done += 1
#
#    print("Employee {} is done with tasks({}/{}):"
#          .format(employeeName, done, len(tasks)))
#
#    for task in done_tasks:
#        print("\t {}".format(task.get('title')))

    csv_file = open('USER_ID.csv', 'w')
    csv_writer = csv.writer(csv_file)

#    count = 0
    for task in tasks:
        row = []
        row.append(employeeId)
        row.append(employeeName)
        row.append(task.get('completed'))
        row.append(task.get('title'))
        csv_writer.writerow(row)

    csv_file.close()
