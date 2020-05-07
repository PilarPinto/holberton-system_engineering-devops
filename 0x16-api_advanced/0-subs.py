#!/usr/bin/python3
'''Gathering data from reddit'''
import requests


def number_of_subscribers(subreddit):

    sub_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    reddit_sub = requests.get(sub_url, allow_redirects=False,
                              headers={'User-Agent': 'My User Agent 1.0'})
    re2j = reddit_sub.json()
    if reddit_sub:
        return (re2j.get('data').get('subscribers'))
    else:
        return (0)
