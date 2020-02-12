#-*- coding:utf-8 -*-
from twitterscraper import query_tweets
import datetime

# tweet crawling with keyword
keyword = '펭수'
startdate = datetime.date(2020,1,1)
stopdate = datetime.date(2020,1,2)
tweet_limit = 1

list_of_tweets = query_tweets(keyword, begindate=startdate, enddate=stopdate, limit=tweet_limit)
#f = open("output.txt", 'w')
for tweet in list_of_tweets:
    print("screen_name: "+tweet.screen_name) #사용자아이디
    print("username: "+tweet.username) #닉네임
    print("user_id: "+tweet.user_id)
    print("tweet_id: "+tweet.tweet_id)
    print("tweet_url: "+tweet.tweet_url)
    print("timestamp: "+str(tweet.timestamp)) #날짜
    print("timestamp_epchs: "+str(tweet.timestamp_epochs))
    print("text: "+tweet.text) #트윗내용
    print("text_html: "+tweet.text_html)
    print("links: "+str(tweet.links))
    print("hashtags: "+str(tweet.hashtags))
    print("has_media: "+str(tweet.has_media))
    print("img_urls: "+str(tweet.img_urls))
    print("video_url: "+str(tweet.video_url))
    print("likes: "+str(tweet.likes))
    print("reweets: "+str(tweet.retweets))
    print("replies: "+str(tweet.replies))
    print("is_replied: "+str(tweet.is_replied))
    print("is_reply_to: "+str(tweet.is_reply_to))
    print("parent_tweet_id: "+tweet.parent_tweet_id)
    print("reply_to_users: "+str(tweet.reply_to_users))

    #f.write(tweet.text) #텍스트
