# auth = tweepy.OAuth1UserHandler(
#    'CSXKbckm6fF00Suve8SZfoYfr', 'tDa1WeyHvrPGbD0dbixkAjnfe8pnMOIIp7pLrEX0EHnBW4fx5u', '1434844694610071552-fzyVKBXawhfdt5ltstOir69IovnvRn','7tfRvw3q63LAlhE8JH75ZmCtZAXoURMYvIg5q0tmGS7cK', 
# )

#bearer_token="7tfRvw3q63LAlhE8JH75ZmCtZAXoURMYvIg5q0tmGS7cK"


import configparser
import tweepy
import pandas as pd
import geocoder
from textblob import TextBlob
import re

api_key = 'CSXKbckm6fF00Suve8SZfoYfr'
api_key_secret = 'tDa1WeyHvrPGbD0dbixkAjnfe8pnMOIIp7pLrEX0EHnBW4fx5u'

access_token = '1434844694610071552-fzyVKBXawhfdt5ltstOir69IovnvRn'
access_token_secret = '7tfRvw3q63LAlhE8JH75ZmCtZAXoURMYvIg5q0tmGS7cK'

# authenticate
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# fetching the location
result=api.search_geo(query="Chile", granularity="country")
place_id = result[0].id

new_search = f"place:{place_id} AND Banco Central -filter:retweets"
public_tweets = api.search_tweets(q=new_search,  tweet_mode="extended",count=100)


# create dataframe
columns = ['Time', 'User', 'Tweet']

data = []
for tweet in public_tweets:
    # print(tweet.created_at)
    # print(tweet.user.screen_name)
    # print(tweet.full_text)
    data.append([tweet.created_at, tweet.user.screen_name, tweet.full_text])


df = pd.DataFrame(data, columns=columns)
for i in df["Tweet"]:
    
    array_texto=i.split(r"[^a-zA-Z0-9]")
    print(array_texto)
    texto=""
    for j in array_texto:
        aux=re.sub(r"[^a-zA-Z0-9]","",j)
        aux=re.sub(r"https","",j)
        aux=re.sub(r"tco","",j)
        aux=''.join(filter(str.isalnum, aux)) 
        
        texto+=f" {aux}"
    print(texto)

    #print(dir(TextBlob(texto)))