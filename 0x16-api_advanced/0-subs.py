#!/usr/bin/python3
" This is a line of text"
import requests


def number_of_subscribers(subreddit):
    " This is a line of text"
    sub = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                       headers={'User-Agent': "hello"})
    if sub.status_code == 200:
        return sub.json().get('data').get('subscribers')
    else:
        return 0
