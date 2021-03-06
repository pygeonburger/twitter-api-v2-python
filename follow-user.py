# THIS SCRIPT ALLOWS YOU TO FOLLOW A SPECIFIC USER

# Import required libraries
import requests, configparser, json
from requests_oauthlib import OAuth1

# Read the keys from auth.ini and define them
config = configparser.ConfigParser()
config.read('backupauth.ini')

CONSUMER_KEY = config.get('credentials', 'consumer_key')
CONSUMER_SECRET = config.get('credentials', 'consumer_secret')
ACCESS_TOKEN = config.get('credentials', 'access_token')
ACCESS_TOKEN_SECRET = config.get('credentials', 'access_token_secret')

oauth = OAuth1(CONSUMER_KEY,
  client_secret=CONSUMER_SECRET,
  resource_owner_key=ACCESS_TOKEN,
  resource_owner_secret=ACCESS_TOKEN_SECRET)

# Put YOUR user ID here
your_id = 1335402487885393921

# Put the ID of the person you want to FOLLOW here (string)
person_to_follow_id = '1299121724684869633'

data = {'target_user_id': person_to_follow_id}

headers = {'Content-type': 'application/json'}

response = requests.post(f"https://api.twitter.com/2/users/{your_id}/following", headers=headers, data=json.dumps(data), auth=oauth)

# Print the response
print(response.json())

# Do whatever you want with the result here after.