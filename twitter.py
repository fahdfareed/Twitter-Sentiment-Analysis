import tweepy
import json
from google.cloud import language_v1



def get_latest_tweet(handle):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    latest = api.user_timeline(screen_name = handle, count = 1, tweet_mode = "extended")
    return [latest[-1]._json["full_text"]]

def get_latest_thirty_tweets(handle):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #get latest 30 tweets
    tweets = []

    latest = api.user_timeline(screen_name = handle, count = 30, tweet_mode = "extended")
    for i in range(len(latest)-1, -1, -1):
        tweets.append(latest[i]._json["full_text"])
    return tweets

def get_latest_searches(keyword):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #get most recent 20 tweets with the given keyword
    tweets = []

    latest = api.search_tweets(q = keyword, count = 30, tweet_mode = "extended", lang = "en")
    for i in range(len(latest)-1, -1, -1):
        tweets.append(latest[i]._json["full_text"])
    return tweets


def get_trends():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #get most recent 20 tweets with the given keyword
    tweets = []
    #print(api.available_trends())
    latest = api.get_place_trends(id = 56013645)
    for i in range(0, len(latest[0]['trends'])):
        tweets.append(latest[0]['trends'][i]['name'])
    return tweets

def sentiment_analysis(tweets):
    client = language_v1.LanguageServiceClient.from_service_account_json()

    analyzed = []
    for i in tweets:
        doc  = language_v1.Document(content=i, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(request={'document': doc}).document_sentiment
        analyzed.append(sentiment)
        print(i)
        print(sentiment.score)
        if (sentiment.score>0.3):
            nature = "Positive"
        elif (sentiment.score < -0.2):
            nature = "Negative"
        else:
            nature = "Neutral"
        print("The Tweet is", nature)
        print("")






if __name__ == '__main__':
    print("What Option do you want?")
    print("1. Latest Tweet \n2. Latest 10 Tweets \n3. Search Keyword \n4. Latest Boston Trend")
    option = input("Enter Now:")
    key = str(input("Enter handle or keyword:"))

    latest = 'a'

    if option == '1':
        latest = sentiment_analysis(get_latest_tweet(key))
    elif option == '2':
        latest = sentiment_analysis(get_latest_thirty_tweets(key))
    elif option == '3':
        latest = sentiment_analysis(get_latest_keyword(key))
    elif option == '4':
        latest = get_trends(key)
        for i in latest:
            print(i)


# latest = sentiment_analysis(get_latest_tweet("@POTUS"))
# try:
#     for i in latest:
#         print(i)
# except:
#     print(latest)