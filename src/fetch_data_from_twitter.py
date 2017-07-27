#!/bin/user/python

#import required libraries
import signal
import sys 
import time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# File path where fetched data will be stored
FILEPATH="../data/twitter_data.txt"

# Secret File Path
SECRETFILEPATH="../secret/auth.txt"

# Open the file
f=open(FILEPATH, 'w')

# Fetch the access token and consumer key from secret folder
def fetch_secret():
	f = open(SECRETFILEPATH, 'r')
	authdict = {}

	for data in f.readlines():
		list = data.split("=")
		authdict[list[0]] = list[1].strip()
	
	access_token        = authdict['access_token']
	access_token_secret = authdict['access_token_secret']
	consumer_key        = authdict['consumer_key']
	consumer_secret     = authdict['consumer_secret']
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	return auth

# Basic listener that just prints received tweets to stdout
class StdOutListener (StreamListener):

	def on_data(self, data):
		global f
		f.write (data)
		return True

	def on_error(self, status):
		global f
		print ("ERROR: ",status)
		f.write (str(status))


# Number of tweets captured
def GetNumOfTweets():
	f = open(FILEPATH, "r")
	count = 0
	for i in f.readlines():
		count = count + 1

	print(str(count)+" Tweets fetched !")
	f.close()


# Signal Handler
def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
	signal.signal(signal.SIGINT, original_sigint)
	global f
	try:
		if input("\nReally quit? (y/n)> ").lower().startswith('y'):
			print("Shutting down...")
			GetNumOfTweets()
			f.close()
			stream.disconnect()
			sys.exit(1)

	except KeyboardInterrupt:
		print("Ok ok, quitting")
		f.close()
		sys.exit(1)

# restore the exit gracefully handler here    
signal.signal(signal.SIGINT, exit_gracefully)

if  __name__ == '__main__':

	# store the original SIGINT handler
	original_sigint = signal.getsignal(signal.SIGINT)

	# Twitter authentication and the connection to Twitter streaming API
	listner = StdOutListener()
	auth = fetch_secret()
	stream = Stream(auth, listner)

	print("Fetching Tweets...")

	# Filter out the Twitter Stream to Capture on Keyword 
	stream.filter(track=['Java'])
