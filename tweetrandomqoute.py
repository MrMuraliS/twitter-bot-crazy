from time import sleep
import tweepy
from tweepy import OAuthHandler
from tweepy.error import RateLimitError, TweepError
import requests

import os
from os import environ
import time

# Authenticate to Twitter
access_token = environ['Access_Token']
access_token_secret = environ['Access_Token_Secret']
consumer_key = environ['API_Key']
consumer_secret = environ['API_secret_Key']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
print('Authenticated')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
# print(user.friends_count)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    except StopIteration:
        print('Done')


""" Randome qoute Tweet """

def random_qoute():
    i = 0
    while True:
        try:

            import  random, json, requests
            randnum = random.randint(0,99)

            response = requests.get('https://www.reddit.com/r/showerthoughts/top.json?sort=top&t=week&limit=100', headers = {'User-agent': 'Showerthoughtbot 0.1'})
            response = json.loads(response.text)

            response = response["data"]["children"][randnum]["data"]["title"]

            api.update_status(response)
            # api.update_status(f'{content}  #{tag} \n\n ~~{author}')
            print(f'Qoute- {i+1} is tweeted')
            time.sleep(60 * 15)
        except TweepError as e:
            print(e.reason)
        except RateLimitError:
            time.sleep(1000)
        i += 1
    # print('All processed')

if __name__ == "__main__":
    random_qoute()