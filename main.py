# libraries
from twitterscraper import query_tweets
from konlpy.tag import Mecab
from wordcloud import WordCloud

from collections import Counter
from tkinter import *
import matplotlib.pyplot as plt
import datetime
import csv

from datacleansing import *

# lbl = label
# txt = Endtry
# rd = radio

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

def getEntries(event):
    keyword = txt_keyword.get()
    beginday = Entry.get(txt_getBeginday)
    endday = Entry.get(txt_getEndday)
    limit = Entry.get(txt_limit)
    begindate = datetime.datetime.strptime(beginday, "%Y%m%d").date()
    enddate = datetime.datetime.strptime(endday, "%Y%m%d").date()
    getTweet(keyword, begindate, enddate, limit)

def korean():
    menubutton['text']="korean"
    lbl_keyword['text']="키워드: "
    lbl_getBeginday['text']="시작날짜: "
    lbl_getEndday['text']="종료날짜: "
    lbl_limit['text']="최대개수: "
    btn['text']="크롤링 시작"

def english():
    menubutton['text']="english"
    lbl_keyword['text']="keyword: "
    lbl_getBeginday['text']="start date: "
    lbl_getEndday['text']="end date: "
    lbl_limit['text']="limitation: "
    btn['text']="start crawling"

def setWidgets(window):
    global menubutton
    global lbl_keyword
    global lbl_getBeginday
    global lbl_getEndday
    global lbl_limit
    global txt_keyword
    global txt_getBeginday
    global txt_getEndday
    global txt_limit
    global btn
    ## MenuButton
    menubutton = Menubutton(window, text = "Language", relief = FLAT)
    menubutton.grid(row=0, column=0)
    menubutton.menu = Menu(menubutton)
    menubutton["menu"]=menubutton.menu
    menubutton.menu.add_checkbutton(label = "Korean", command = korean)
    menubutton.menu.add_checkbutton(label = "English", command = english)
    # Label
    lbl_keyword = Label(window, text="키워드: ")
    lbl_getBeginday = Label(window, text="시작날짜: ")
    lbl_getEndday = Label(window, text="종료날짜: ")
    lbl_limit = Label(window, text="최대개수: ")
    lbl_keyword.grid(row=1, column=0)
    lbl_getBeginday.grid(row=2, column=0)
    lbl_getEndday.grid(row=3, column=0)
    lbl_limit.grid(row=4, column=0)
    ## Endtry
    txt_keyword = Entry(window)
    txt_getBeginday = Entry(window)
    txt_getEndday = Entry(window)
    txt_limit = Entry(window)
    txt_keyword.grid(row=1, column=1)
    txt_getBeginday.grid(row=2, column=1)
    txt_getEndday.grid(row=3, column=1)
    txt_limit.grid(row=4, column=1)
    ## Button
    btn = Button(window, text="크롤링 시작")
    btn.grid(row=5, column=0)
    btn.bind('<Button-1>',getEntries)

def main():
    window = Tk()
    window.title("Twitter Crawler")
    #window.geometry("300x300")
    setWidgets(window)
    window.mainloop()

if __name__ == '__main__':
    main()
