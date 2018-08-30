#!/usr/bin/python3
''' module for function to return top 10 hot posts of a given subreddit '''
import requests
import sys


def top_ten(subreddit):
    '''
    Args:
        subreddit: subreddit name
    Returns:
        top ten post titles
        or None if queried subreddit is invalid
    '''
    a = {'User-agent': 'ubuntu:hsed0x16app:v0.1 (by /u/325sf/)'}

    url = 'http://www.reddit.com/r/{sr}/hot.json?limit=10'.format(sr=subreddit)
    r = requests.get(url, headers=a)

    stat = r.status_code
    try:
        subr = r.json()['data']['children'][0]['data']['subreddit']
    except:
        print(None)
        return

    if stat != 200 or subr != subreddit:
        print(None)
        return

    for hot_item in r.json()['data']['children']:
        print(hot_item['data']['title'])


if __name__ == '__main__':
    try:
        s = sys.argv[1]
    except:
        print('Usage: ./1-top_ten.py <subreddit>')
    top_ten(s)
