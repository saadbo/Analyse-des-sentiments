import string
from collections import Counter

import matplotlib.pyplot as plt


def get_tweets(tweet_word,maxtw):
    import GetOldTweets3 as got
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(tweet_word) \
        .setSince("2020-06-01") \
        .setUntil("2020-06-30") \
        .setMaxTweets(maxtw)
    # Creation of list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    # Creating list of chosen tweet data
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets


