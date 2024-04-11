#!/usr/bin/python3
"""Subscribers API Module"""
import requests


def number_of_subscribers(subreddit):
    """Method that return the number of subs"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    if response.status_code >= 300:
        return 0
    else:
        subscribers = response.json().get("data").get("subscribers")
        return subscribers
