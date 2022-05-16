#!/usr/bin/python3
'''
Records all tasks that are owned by this employee
'''


import requests
from sys import argv
import csv

url = "https://jsonplaceholder.typicode.com/users"


def main():
    '''
    main function that not be executable if not main
    '''
    username = requests.get("{}/{}".format(url, argv[1])).json()
    user_tasks = requests.get("{}/{}/todos".format(url, argv[1])).json()

    if username and user_tasks:
        with open('{}.csv'.format(argv[1]), mode='w') as csv_file:
            writer = csv.writer(csv_file,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_ALL)

            for value in user_tasks:
                writer.writerow([value['userId'],
                                 username['username'],
                                 value['completed'],
                                 value['title']])


if __name__ == '__main__':
    if len(argv) > 1 and argv[1].isdigit():
        main()
