import tweepy
import json
from google.cloud import language_v1
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from PIL import Image
import os
import io



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

    #get most recent 30 tweets with the given keyword
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
    client = language_v1.LanguageServiceClient.from_service_account_json("")

    analyzed = []
    scored = []
    for i in tweets:
        doc  = language_v1.Document(content=i, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(request={'document': doc}).document_sentiment
        analyzed.append(sentiment)
        #print(i)
        #print(sentiment.score)
        if (sentiment.score>0.3):
            nature = "Positive"
        elif (sentiment.score < -0.2):
            nature = "Negative"
        else:
            nature = "Neutral"
        scored.append(nature)
        #print("The Tweet is", nature)
        #print("")
    return scored






# if __name__ == '__main__':
#     print("What Option do you want?")
#     print("1. Latest Tweet \n2. Latest 10 Tweets \n3. Search Keyword \n4. Latest Boston Trend")
#     option = input("Enter Now:")
#     key = str(input("Enter handle or keyword:"))

#     latest = 'a'

#     if option == '1':
#         latest = sentiment_analysis(get_latest_tweet(key))
#     elif option == '2':
#         latest = sentiment_analysis(get_latest_thirty_tweets(key))
#     elif option == '3':
#         latest = sentiment_analysis(get_latest_keyword(key))
#     elif option == '4':
#         latest = get_trends(key)
#         for i in latest:
#             print(i)

if __name__ == '__main__':
    latest_tweet = get_latest_tweet("@POTUS")
    sentiment = sentiment_analysis(latest_tweet)[0]
    latest_tweet = latest_tweet[0]
    sentiment = "The Tweet is " + sentiment

    #reactions = sentiment_analysis(get_latest_thirty_tweets("Biden"))
    reactions =["Positive", "Negative", "Neutral" ,"Positive", "Negative", "Neutral", "Neutral","Positive", "Negative", "Neutral","Positive", "Negative", "Neutral","Positive", "Negative", "Neutral","Positive", "Negative", "Neutral"]
    summed = {"Positive":0, "Neutral":0, "Negative":0}
    for i in reactions:
        summed[i] += 1/30

    plt.bar(summed.keys(), summed.values())
    plt.savefig("myplot")
    img = Image.open(os.getcwd()+"/myplot.png")
    img.thumbnail((800, 800))
    bio = io.BytesIO()
    img.save(bio, format="PNG")


    layout = [[sg.Text("President Biden:", font= ("Arial", 25)),],  
    [(sg.Text(latest_tweet, text_color="Black", font = ("Arial", 15) , size=(100, 4), background_color='white'))],
    [sg.Text(sentiment, text_color = "Black", font = ("Times New Roman", 18))] ,
    [sg.Image(data= bio.getvalue())],
    [sg.Button("Don't Show Me Anymore")]]

    window = sg.Window("Biden", layout, size=(1200, 800))

    while True:
        event, values = window.read()

        if event == "Don't Show Me Anymore" or event == sg.WIN_CLOSED:
            break
        
        if event == "Show Plot":
            plt.show(block=False)
 
    
    window.close()
