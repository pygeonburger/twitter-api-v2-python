# This script allows you to hide/unhide specific replies to your Tweets. In order to do this, you must know this tweets status ID

# Import required libraries
import requests, configparser, json
from requests_oauthlib import OAuth1

# Read the keys from auth.ini and define them
config = configparser.ConfigParser()
config.read('auth.ini')

CONSUMER_KEY = config.get('credentials', 'consumer_key')
CONSUMER_SECRET = config.get('credentials', 'consumer_secret')
ACCESS_TOKEN = config.get('credentials', 'access_token')
ACCESS_TOKEN_SECRET = config.get('credentials', 'access_token_secret')

oauth = OAuth1(CONSUMER_KEY,
  client_secret=CONSUMER_SECRET,
  resource_owner_key=ACCESS_TOKEN,
  resource_owner_secret=ACCESS_TOKEN_SECRET)

headers = {'content-type': 'application/json'}

# Put the status ID of the Tweet you want to hide/unhide here. The one that's already here is one that is in reply to my account, so you will need to replace it with a status that replies to your own tweet in order for this to work.
status_id = 1349331895771942913

# CHANGE THIS TO FALSE IF YOU WANT TO UNHIDE A REPLY
params = {
  'hidden': True
}

response = requests.put(f"https://api.twitter.com/2/tweets/{status_id}/hidden", data=json.dumps(params), headers=headers, auth=oauth)

# Will return an indicator of whether the Tweet is hidden or not (true or false)
print(response.json())
