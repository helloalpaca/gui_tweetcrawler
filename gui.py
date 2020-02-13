from twitterscraper import query_tweets
from tkinter import *
import datetime
import csv

# lbl = label
# txt = Endtry

def getEntries(event):
    keyword = txt_keyword.get()
    beginday = Entry.get(txt_getBeginday)
    endday = Entry.get(txt_getEndday)
    limit = Entry.get(txt_limit)
    begindate = datetime.datetime.strptime(beginday, "%Y%m%d").date()
    enddate = datetime.datetime.strptime(endday, "%Y%m%d").date()
    getTweet(keyword, begindate, enddate)

def getTweet(keyword, begindate, enddate):
    f = open('files/'+keyword+'_raw.csv','w',encoding='utf-8-sig',newline='')
    writer = csv.writer(f,delimiter=',')

    # crawling data using twitterscraper
    list_of_tweets = query_tweets(keyword, begindate=begindate, enddate=enddate, limit=10)

    for tweet in list_of_tweets:
        writer.writerow([tweet.screen_name, tweet.username, tweet.timestamp, tweet.text])
    f.close()

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
