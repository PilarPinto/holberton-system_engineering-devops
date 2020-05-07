#!/usr/bin/python3
'''
Gathering recursive ten reddit
programming posts (hot)
'''
import requests


def recurse(subreddit, hot_list=[], after_val=None):

    sub_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    reddit_sub = requests.get(sub_url, allow_redirects=False,
                              headers={'User-Agent': 'My User Agent 1.0'},
                              params={
                                  'limit': 100,
                                  'after': after_val
                              })
    if reddit_sub.status_code == 200:
        re2j = reddit_sub.json()
        access_data = re2j.get('data').get('children')
        after_val = re2j.get('data').get('after')

        for ind in access_data:
            hot_list.append(ind.get('data').get('title'))

        if not after_val:
            return (hot_list)
        return (recurse(subreddit, hot_list, after_val))
    else:
        return(None)
