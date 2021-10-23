import tweepy
import json
from google.cloud import language_v1
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from PIL import Image
import os
import io


# Twitter API Keys
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""
path_key = ""

def authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return tweepy.API(auth)

# Returns the latest Tweet of the provided username
def get_latest_tweet(handle):
    
    api = authenticate()
    latest = api.user_timeline(screen_name = handle, count = 1, tweet_mode = "extended")
    return [latest[-1]._json["full_text"]]

# Returns the top thirty Tweets of the provided username
def get_latest_thirty_tweets(handle):
    
    api = authenticate()
    tweets = []
    latest = api.user_timeline(screen_name = handle, count = 30, tweet_mode = "extended")
    for i in range(len(latest)-1, -1, -1):
        tweets.append(latest[i]._json["full_text"])
    return tweets

# Returns the top 30 Tweets that contain the keyword searched for
def get_latest_searches(keyword):
    
    api = authenticate()
    tweets = []
    latest = api.search_tweets(q = keyword, count = 30, tweet_mode = "extended", lang = "en")
    for i in range(len(latest)-1, -1, -1):
        tweets.append(latest[i]._json["full_text"])
    return tweets

# Returns the top trends given the Twitter Area Code
def get_trends(code = 56013645):
    
    api = authenticate()
    tweets = []
    latest = api.get_place_trends(id = code)
    for i in range(0, len(latest[0]['trends'])):
        tweets.append(latest[0]['trends'][i]['name'])
    return tweets

# Used to conduct Sentimental Analysis on a list of tweets
# Returns a list characterizing the nature of the Tweets
def sentiment_analysis(tweets):
    # Set Client
    client = language_v1.LanguageServiceClient.from_service_account_json(path_key)

    analyzed = []
    scored = []
    for i in tweets:
        # Get the analysis score from Google NLP
        doc  = language_v1.Document(content=i, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(request={'document': doc}).document_sentiment
        analyzed.append(sentiment)

        # Categorise the score as Positive/ Negative/ Neutral
        if (sentiment.score > 0.3):
            nature = "Positive"
        elif (sentiment.score < -0.2):
            nature = "Negative"
        else:
            nature = "Neutral"
        scored.append(nature)
    return scored




# Allowing user to enter the values
def user_main(): 
    print("What Option do you want?")
    print("1. Latest Tweet \n2. Latest 10 Tweets \n3. Search Keyword \n4. Latest Boston Trend")
    option = input("Enter Now:")
    key = str(input("Enter handle or keyword:"))

    # get single tweet
    if option == '1':
        latest = sentiment_analysis(get_latest_tweet(key))
    # get 30 tweets
    elif option == '2':
        latest = sentiment_analysis(get_latest_thirty_tweets(key))
    # get tweets related to a keyword
    elif option == '3':
        latest = sentiment_analysis(get_latest_keyword(key))
    # get latest trends for Boston
    elif option == '4':
        latest = get_trends()
        for i in latest:
            print(i)

# Preset values adhering to the project ""
def auto_main():

    # Get latest Tweet for POTUS and conduct a sentiment analysis
    latest_tweet = get_latest_tweet("@POTUS")[0]
    sentiment = "The Tweet is " + sentiment_analysis(latest_tweet)[0]

    # Get sentiment of latest Tweets containing Biden
    reactions = sentiment_analysis(get_latest_searches("Biden"))
    summed = {"Positive":0, "Neutral":0, "Negative":0}
    for i in reactions:
        summed[i] += 1/30

    # Plot a barchart with the categories
    plt.bar(summed.keys(), summed.values())
    plt.savefig("myplot")
    img = Image.open(os.getcwd()+"/myplot.png")
    img.thumbnail((800, 800))
    bio = io.BytesIO()
    img.save(bio, format="PNG")

    # GUI Implementation
    # Presidents Tweet, Sentiment, Barchart, Close Button
    layout = [[sg.Text("President Biden:", font= ("Arial", 25)),],  
    [(sg.Text(latest_tweet, text_color="Black", font = ("Arial", 15) , size=(100, 4), background_color='white'))],
    [sg.Text(sentiment, text_color = "Black", font = ("Times New Roman", 18))] ,
    [sg.Image(data= bio.getvalue())],
    [sg.Button("Don't Show Me Anymore")]]

    window = sg.Window("Biden", layout, size=(1200, 800))

    # Closing the window conditions
    while True:
        event, values = window.read()
        if event == "Don't Show Me Anymore" or event == sg.WIN_CLOSED:
            break
        if event == "Show Plot":
            plt.show(block=False)
 
    window.close()

if __name__ == '__main__':
    user_choice = input("If you want to see President Bidens Tweets and Approval enter 1")
    if user_choice == 1:
        auto_main()
    else:
        user_main()