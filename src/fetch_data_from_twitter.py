#!/bin/user/python

#import required libraries
import utils as ut
import signal
import sys
import time
from tweepy.streaming import StreamListener
from tweepy import Stream

# Open the file
f=open(ut.FILEPATH, 'w')

# Basic listener that just prints received tweets to stdout
class TwitterListener (StreamListener):

	def __init__(self, phrases):
		# Get access to twitter api
		auth = ut.fetch_secret()
		self.__stream = Stream(auth, listener=self)
		print("Fetching Tweets...")
		self.__stream.filter(track=phrases)

	def on_data(self, data):
		global f
		f.write (data)
		return True

	def on_error(self, status):
		global f
		print ("ERROR: ",status)
		f.write (str(status))

# Signal Handler
def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
	signal.signal(signal.SIGINT, original_sigint)
	global f
	try:
		if input("\nReally quit? (y/n)> ").lower().startswith('y'):
			print("Shutting down...")
			f.close()
			ut.GetNumOfTweets()
			#stream.disconnect()
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

	phrases = []
	# Take input Phrase from user 
	phrase = input("\nEnter search phrase: ")
	phrases.append(phrase)

	# Twitter authentication and the connection to Twitter streaming API
	listner = TwitterListener(phrases)
