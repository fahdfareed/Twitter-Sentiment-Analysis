# Twitter-Sentiment-Analysis
In this project we use the Twitter API to get different tweets and then by using the Google NLP API we analyze the tweets to get a meaningful output.


## Twitter API
The following functions were created taht perform different tasks. Here is a description of each function, their inputs and their outputs.

### GET_LATEST_TWEET
This function takes in the *handle* of the instagram user for which you want the most recent tweet and outputs an *array* that contains the tweet. It authenticates the user using Twitter API Keys and then gets the most recent tweet and diplays it. This function can be used to update the arrays of a user after set intervals and display the tweet incase there is a new tweet present.

### GET_LATEST_THIRTY_TWEETS

This function takes in the *handle* of the instagram user for which you want the most recent tweet and outputs an *array* that contains a list of the most recent tweets. It authenticates the user using Twitter API Keys and then gets the most recent 30 tweets. This function can be used to get a sentiment analysis of the latest tweets to know how the mood of that perticular person is.

### GET_LATEST_SEARCHES

This function takes in a keyword that is then used to query the top fifty results of that keyword. The list of tweets is returned. This is an extremely important function that can be used to tell us an analysis of the sentiment of the people regarding a given keyword. In the following Prokect, this plays a significant role.

### GET_TRENDS

This function returns a list of the most recent trends within the Boston Metropolitan Area. This is an important function that can help us identify top trends which can then be used to do a sentimental analysis on the tweets for those top trends. 


## Google NLP

This application uses the Google NLP to find the various sentiments of a given statement and then classifies them into Positive, Negative or Neutral

### SENTIMENT_ANALYSIS

The function takes in a list of arrays of Tweets and then uses the Google NLP API to find their sentiment. It then classifies them into Positive, Negative or Neutral according to a predefined threshold and then prints out the Tweets and their Sentiment.


# Sentimental Analysis for the Tweets of the President of Unites States.
In this project I use Google's NLP API and Twitter API to get an analysis of what the sentiment of the president of the United State is given his declining popularity. Essentially we will get the top Tweets from the Twitter API and then analyze how the president currently feel.

With every tweet we will then do a query search with the name of the President or some other parameter and compare the trends of how the people's reaction is to the President.

### User Stories

1. As a user I want to *get the latest trends* so that I can get the news.

2. As a user I want to *get the latest tweet for a particular user* so that I can stay updated.

3. As a user I want to *get a list of most recent tweets of any user* without having to open Twitter.

4. As a user I want to *get a sentimental analysis of the most recent tweet of a user* to know what their mood is.

5. As a user I want to *get an analysis of the past few tweets* to be able to predict the mood of a particular user.

6. As a user I want to *search a particular keyword* and get the tweets associated with it.

7. As a user I want to *get a sentimental analysis* of the tweets which are the result of a particular query.

8. As a user I want the option to be able to get the latest tweet of the President and a sentiment of how users feel about him.

## GUI
This project uses the PySimpleGUI library something that I have been using for the first time. It provided me with a great skillset on incorporating different GUI items such as images, text, multiline and ButTons on my application. It added a much needed user display interface as the application itself did not rely on any user input. It can now be run by anyone without any knowledge of Python.

### Running the Application
Clone the application and use python3 to run the twitter.py file. Ensure you have tweepy and google.cloud
