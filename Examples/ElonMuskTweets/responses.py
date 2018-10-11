import tweepy
import random

try:
	from keys import *
	# Consumer keys and access tokens, used for OAuth
except:
	consumer_key = raw_input("Consumer Key: ")
	consumer_secret = raw_input("Consumer Secret: ")
	access_token = raw_input("Access Token: ")
	access_token_secret = raw_input("Access Token Secret: ")

def get_tweet():
	# OAuth process, using the keys and tokens
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	items = []
	# Creation of the actual interface, using authentication
	api = tweepy.API(auth)
	for status in tweepy.Cursor(api.user_timeline, screen_name='@elonmusk').items(200):
		if '@' not in status._json['text']:
			items.append(status._json['text'])
	return random.choice(items)
