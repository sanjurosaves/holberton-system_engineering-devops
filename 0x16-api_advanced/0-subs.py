#!/usr/bin/python3
''' module for function to return number of subreddit subscribers '''
import requests
import sys


def number_of_subscribers(subreddit):
    '''
    Args:
        subreddit: subreddit name
    Returns:
        number of subscribers to the subreddit,
        or 0 if subreddit requested is invalid
    '''
    a = {'User-agent': 'ubuntu:hsed0x16app:v0.1 (by /u/325sf/)'}

    url = 'http://www.reddit.com/r/{sr}/about.json'.format(sr=subreddit)
    r = requests.get(url, headers=a)

    try:
        subs = r.json()['data']['subscribers']
    except:
        return 0
    try:
        subr = r.json()['data']['display_name']
    except:
        return 0
    stat = r.status_code

    if stat == 200 and subr == subreddit:
        return subs

    return 0

if __name__ == '__main__':
    try:
        s = sys.argv[1]
    except:
        print('Usage: ./0-subs.py <subreddit>')
    print(number_of_subscribers(s))
