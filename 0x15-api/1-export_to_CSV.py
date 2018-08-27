#!/usr/bin/python3
''' exports data in the CSV format '''
import csv
import requests
import sys


def gather_data():
    ''' gathers data from api '''
    try:
        userid = sys.argv[1]
    except:
        print('Usage: ./1-export_to_CSV.py <employee id>')
        return

    userurl = 'https://jsonplaceholder.typicode.com/users'

    t = requests.get(userurl+'/'+userid+'/todos')
    u = requests.get(userurl+'/'+userid)

    user_dict = u.json()
    try:
        emp_name = (user_dict['username'])
    except:
        print("Employee does not exist.")
        return

    task_vals = []

    for i in t.json():
        std = {}
        std['user_id'] = i['userId']
        std['user_name'] = emp_name
        std['status'] = i['completed']
        std['title'] = i['title']
        task_vals.append(std)

    return task_vals


def save_to_csv(data):
    ''' saves data to csv file '''
    f = 'SER_ID.csv'

    with open(f, 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, delimiter=',', lineterminator='\n',
                                quoting=csv.QUOTE_ALL)

        for k in data:
            taskwriter.writerow([k['user_id'], k['user_name'], k['status'],
                                 k['title']])


if __name__ == '__main__':
    task_list = gather_data()
    save_to_csv(task_list)
