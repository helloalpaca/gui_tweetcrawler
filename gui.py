from twitterscraper import query_tweets
from tkinter import *
from datacleansing import *
import datetime
import csv
from konlpy.tag import Mecab
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# lbl = label
# txt = Endtry
# rd = radio

def getEntries(event):
    keyword = txt_keyword.get()
    beginday = Entry.get(txt_getBeginday)
    endday = Entry.get(txt_getEndday)
    limit = Entry.get(txt_limit)
    begindate = datetime.datetime.strptime(beginday, "%Y%m%d").date()
    enddate = datetime.datetime.strptime(endday, "%Y%m%d").date()
    #getTweet(keyword, begindate, enddate, limit)
"""
def saveCSV(keyword, list_of_tweets):
    # save raw data to csv file
    f = open('files/'+keyword+'_raw.csv','w',encoding='utf-8-sig',newline='')
    writer = csv.writer(f,delimiter=',')
    for tweet in list_of_tweets:
        writer.writerow([tweet.screen_name, tweet.username, tweet.timestamp, tweet.text])
    f.close()

def dataCleansing(text):
    text = clean_http(text)
    text = clean_pic(text)
    text = clean_ATtag(text)
    text = clean_specialsymbol(text)
    text = clean_consonant_vowels(text)
    return text

def morphsAnalyze(keyword, text):
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
    makeWordCloud(keyword, lists)

def makeWordCloud(keyword, lists):
    wordcloud = WordCloud(font_path = 'files/NanumGothicExtraBold.otf',background_color='white', width=1500, height=1000).generate_from_frequencies(lists)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig('files/'+keyword+'_wordcloud.png')

def getTweet(keyword, begindate, enddate, limit):
    # crawling data using twitterscraper
    text=""
    list_of_tweets = query_tweets(keyword, begindate=begindate, enddate=enddate, limit=int(limit))
    saveCSV(keyword, list_of_tweets)
    for tweet in list_of_tweets:
        text = text + tweet.text + "\n"
    text = dataCleansing(text)
    morphsAnalyze(keyword, text)
"""
def main():
    window = Tk()
    window.title("Twitter Crawler")
    #window.geometry("300x300")

    lbl_keyword = Label(window, text="키워드: ")
    lbl_getBeginday = Label(window, text="시작날짜: ")
    lbl_getEndday = Label(window, text="종료날짜: ")
    lbl_limit = Label(window, text="최대개수: ")
    lbl_keyword.grid(row=0, column=0)
    lbl_getBeginday.grid(row=1, column=0)
    lbl_getEndday.grid(row=2, column=0)
    lbl_limit.grid(row=3, column=0)

    global txt_keyword
    global txt_getBeginday
    global txt_getEndday
    global txt_limit

    txt_keyword = Entry(window)
    txt_getBeginday = Entry(window)
    txt_getEndday = Entry(window)
    txt_limit = Entry(window)
    txt_keyword.grid(row=0, column=1)
    txt_getBeginday.grid(row=1, column=1)
    txt_getEndday.grid(row=2, column=1)
    txt_limit.grid(row=3, column=1)

    btn = Button(window, text="입력", width=5)
    btn.grid(row=4, column=0)
    btn.bind('<Button-1>',getEntries)

    window.mainloop()

if __name__ == '__main__':
    main()
