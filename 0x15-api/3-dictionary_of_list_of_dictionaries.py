#!/usr/bin/python3
''' exports data in the JSON format '''
import json
import requests
import sys
from collections import OrderedDict


def gather_data():
    ''' retrieves data from the api '''
    userurl = 'https://jsonplaceholder.typicode.com/users'

    u = requests.get(userurl)

    user_list = u.json()
    eid_list = []
    for user in user_list:
        user_dict = user
        task_dict = {}
        task_vals = []
        user_task_dict = {}
        t = requests.get(userurl+'/'+str(user_dict['id'])+'/todos')
        for i in t.json():
            std = OrderedDict()
            std['username'] = user_dict['username']
            std['task'] = i['title']
            std['completed'] = i['completed']
            task_vals.append(std)
        task_dict[str(user_dict['id'])] = task_vals
        user_task_dict.update(task_dict)

    return user_task_dict


def save_to_json(data):
    ''' saves data to JSON '''
    f = 'USER_ID.json'
    with open(f, mode='w', encoding="UTF8") as fd:
        json.dump(data, fd)


if __name__ == '__main__':
    task_dict = gather_data()
    save_to_json(task_dict)
