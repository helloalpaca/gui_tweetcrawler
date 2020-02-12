#-*- coding:utf-8 -*-
from twitterscraper import query_tweets
import datetime
import csv

from datacleansing import *

from konlpy.tag import Mecab
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# tweet crawling with keyword
keyword = '코로나'
startdate = datetime.date(2020,2,1)
stopdate = datetime.date(2020,2,2)
tweet_limit = 100

# save rawdata to csv file
f = open('files/'+keyword+'_raw.csv','w',encoding='utf-8-sig',newline='')
writer = csv.writer(f,delimiter=',')

# crawling data using twitterscraper
list_of_tweets = query_tweets(keyword, begindate=startdate, enddate=stopdate, limit=tweet_limit)

text = ""
for tweet in list_of_tweets:
    writer.writerow([tweet.screen_name, tweet.username, tweet.timestamp, tweet.text])
    text = text + tweet.text + "\n"
f.close()

# data cleansing
text = clean_http(text)
text = clean_pic(text)
text = clean_ATtag(text)
text = clean_specialsymbol(text)
text = clean_consonant_vowels(text)

# morphological analysis
mecab = Mecab()
morphs = []
words = []

morphs = mecab.pos(text)
for word, tag in morphs:
    if tag in ['NNG']:
        words.append(word)

count = Counter(words)
lists = dict(count.most_common())
print(lists)

# make wordcloud
wordcloud = WordCloud(font_path = 'files/NanumGothicExtraBold.otf',background_color='white', width=1500, height=1000).generate_from_frequencies(lists)
plt.axis('off')
plt.savefig('files/'+keyword+'_wordcloud.png')
