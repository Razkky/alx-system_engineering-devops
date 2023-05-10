#!/usr/bin/python3
""""This module uses the redit api to get th number of subscribers
    for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """This function uses the request module to access the redit api"""
    if subreddit:
        abouts = requests.get(
                 "https://www.reddit.com/r/{}/about.json".format(subreddit),
                 headers={"User-Agent": "My-User-Agent"},
                 allow_redirects=False)
        if abouts.status_code >= 300:
            return 0
        abouts = abouts.json()
        subscriber = abouts['data']['subscribers']
        return subscriber
