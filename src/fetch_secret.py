#!/bin/usr/python

# Secret File Path
SECRETFILEPATH="./secret/auth.txt"

# Fetch the access token and consumer key from secret folder
def fetch_secret():
	f = open(SECRETFILEPATH, 'r')
	authdict = {}

	for data in f.readlines():
#		print (data)
#		print (type(data))
#		print(data.split("="))
		list = data.split("=")
		authdict[list[0]] = list[1]
#		print(list[0]," " ,list[1])
#		print(authdict)
    
	access_token 		= authdict['access_token']
	access_token_secret = authdict['access_token_secret']
	consumer_key		= authdict['consumer_key']
	consumer_secret		= authdict['consumer_secret']

	print('access_token={}'.format(access_token))
	print('access_token_secret = ', access_token_secret)
	print('consumer_key = ', 		consumer_key)
	print('consumer_secret = ', 	consumer_secret)
	print(access_token)
	print('access_token_secret = ', access_token_secret)
	print('consumer_key = ', 		consumer_key)
	print('consumer_secret = ', 	consumer_secret)



def main():
	print("Get the Secret..")
	fetch_secret()

if __name__ == '__main__':
	main()
	
