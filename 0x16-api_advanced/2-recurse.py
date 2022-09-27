#!/usr/bin/python3
" This is a line of text "
import requests


def recurse(subreddit, hot_list=[], after=None):
    " This is a line of text "
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'hello'}
    params = {'after': after}
    sub = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)
    if sub.status_code != 200:
        return None
    for child in sub.json().get('data').get('children'):
        hot_list.append(child.get('data').get('title'))
    after = sub.json().get('data').get('after')
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
