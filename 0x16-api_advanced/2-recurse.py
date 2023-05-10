#!/usr/bin/python3
"""This module uses recursion to quarry reddit api"""
import requests


def recurse(subreddit, hot_list=[], after="None"):
    """Get all the title of a subreddit"""

    posts = requests.get(
        "https://www.reddit.com/r/{}/hot.json"
        .format(subreddit),
        params={"after": after},
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False
         )
    if posts.status_code >= 400:
        return None
    else:
        children = posts.json().get('data').get('children')
        hot_list.append([child.get('data').get('title')
                        for child in children])
        after = posts.json().get('data').get('after')
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)
