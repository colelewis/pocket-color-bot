from random import randint
from twitter_secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_KEY_SECRET, twitter_secrets as ts
import tweepy
import webcolors

consumer_key = ts.API_KEY
consumer_secret = ts.API_KEY_SECRET
access_token = ts.ACCESS_TOKEN
access_secret = ts.ACCESS_TOKEN_SECRET

def main():
    # auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    # auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    # api = tweepy.API(auth)

    # api.update_status('tweet')    
    random_rgb = (randint(0, 255), randint(0, 255), randint(0, 255))
    

if __name__=="__main__":
    main()