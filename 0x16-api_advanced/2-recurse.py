#!/usr/bin/python3
''' module for function to return top 10 hot posts of a given subreddit '''
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    '''
    Args:
        subreddit: subreddit name
        hot_list: list of hot titles in subreddit
        after: last hot_item appended to hot_list
    Returns:
        a list containing the titles of all hot articles for the subreddit
        or None if queried subreddit is invalid
    '''
    a = {'User-agent': 'ubuntu:hsed0x16app:v0.1 (by /u/325sf/)'}

    if after is None:
        url = 'http://www.reddit.com/r/{sr}/hot.json?limit=100'.format(
            sr=subreddit)
    else:
        url =\
            'http://www.reddit.com/r/{sr}/hot.json?limit=100&after={af}'\
            .format(sr=subreddit, af=after)

    r = requests.get(url, headers=a)

    stat = r.status_code
    try:
        subr = r.json()['data']['children'][0]['data']['subreddit']
    except:
        return(None)

    if stat != 200 or subr != subreddit:
        return(None)

    for hot_item in r.json()['data']['children']:
        hot_list.append(hot_item['data']['title'])

    if r.json()['data']['after'] is not None:
        after = r.json()['data']['after']
    else:
        return(hot_list)

    return(recurse(subreddit, hot_list, after))


if __name__ == '__main__':
    try:
        s = sys.argv[1]
    except:
        print('Usage: ./2-recurse.py <subreddit>')
    print(recurse(s))
