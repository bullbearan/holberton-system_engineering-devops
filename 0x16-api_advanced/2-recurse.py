#!/usr/bin/python3
"This is a line of text"
import requests


def recurse(subreddit, hot_list=[], after=None):
    " This is a line of text"
    url = "https://www.reddit.com"
    sub = requests.get(f"{url}/r/{subreddit}/hot.json?after={after}",
                       headers={'User-Agent': "hello"})
    if sub.status_code == 200:
        for child in sub.json().get("data").get("children"):
            hot_list.append(child.get("data").get("title"))
        after = sub.json().get("data").get("after")
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
