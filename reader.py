# auth = tweepy.OAuth1UserHandler(
#    'CSXKbckm6fF00Suve8SZfoYfr', 'tDa1WeyHvrPGbD0dbixkAjnfe8pnMOIIp7pLrEX0EHnBW4fx5u', '1434844694610071552-fzyVKBXawhfdt5ltstOir69IovnvRn','7tfRvw3q63LAlhE8JH75ZmCtZAXoURMYvIg5q0tmGS7cK',
# )

#bearer_token="7tfRvw3q63LAlhE8JH75ZmCtZAXoURMYvIg5q0tmGS7cK"
from GoogleNews import GoogleNews
import pandas as pd
import configparser
import tweepy
import pandas as pd
import geocoder
from textblob import TextBlob
import re
cadena_con_acentos = 'áéíóú'
import unidecode




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

new_search = f"place:{place_id} AND Banco Central AND Chile -filter:retweets"
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

todos=[]

#Agrego todos los tweets
for i in df["Tweet"]:

    array_texto=i.split(r"[^a-zA-Z0-9]")
    texto=unidecode.unidecode(array_texto[0])
    texto = re.sub(r"http\S+", " ",texto)
    texto=re.sub(r"[^a-zA-Z0-9]"," ",texto)
    todos.append(texto)


#cargo los elementos desde google news
news = GoogleNews(start='11/01/2022',end='11/29/2022',lang='es',encode='utf-8')
news.search("Banco Central de Chile",)
result = news.result()
data = pd.DataFrame.from_dict(result)
data = data.drop(columns=["img"])
data.head()
for res in result:
    texto=res["title"]+" "+res["desc"]
    texto=unidecode.unidecode(texto)
    texto = re.sub(r"http\S+", " ",texto)
    texto=re.sub(r"[^a-zA-Z0-9]"," ",texto)
    todos.append(texto)

from googletrans import Translator
translator = Translator()

print(todos)
df = pd.DataFrame(todos, columns=['es'])
print(df )

for i in df['es']:
    try:
        print(translator.translate(i).text)
    except Exception:
        print(Exception)


#print(tb.sentiment)
