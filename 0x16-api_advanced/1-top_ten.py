#!/usr/bin/python3
" This is a line of text"
import requests


def top_ten(subreddit):
    " This is a line of text"
    sub = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                       headers={'User-Agent': "hello"}, params={'limit': 10})
    if sub.status_code == 200:
        for child in sub.json().get('data').get('children'):
            print(child.get('data').get('title'))
    else:
        print(None)
