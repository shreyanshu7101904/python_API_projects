from tkinter import *
import requests
import pandas as pd
import time

x = time.localtime()[0:6]
fname = ""
for i in x:
    fname = fname + str(i)
fname = fname + ".csv"
print(fname)
def fetch_news(query):
    query = str(query)
    # BBC news api
    # main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4c06371c000b4c52bb6b4520334dafc6"
    # main_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=4c06371c000b4c52bb6b4520334dafc6"
    main_url = "https://newsapi.org/v2/everything?q=" + query + \
               "&sortBy=publishedAt&apiKey=4c06371c000b4c52bb6b4520334dafc6"
    # main_url = "https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=4c06371c000b4c52bb6b4520334dafc6"
    # fetching data in json format
    open_bbc_page = requests.get(main_url).json()
    key = open_bbc_page.keys()
    print(key)
    content = {'Data_CSV': open_bbc_page['articles'] for keys in key}
    # print(content)
    print(content.keys())
    # print(open_bbc_page)
    # getting all articles in a string article
    df = pd.DataFrame(content)
    # print(df)
    df2 = df["Data_CSV"].apply(pd.Series)
    df2.to_csv(fname)

    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []
    author = []
    desc = []
    link = []
    for x in article:
        results.append(x["title"])
        author.append(x["author"])
        desc.append(x["description"])
        link.append(x["url"])
    final = zip(author, results, desc, link)
    print(final)
    count = 1
    for i, j, k, l in final:
        print(count)
        print("\tAuthor :", i)
        print("\tTitle  :", j)
        print("\tNews   :", k)
        print("\tLink   :", l)
        count += 1


window = Tk()
window.wm_title("NEWS")
l1 = Label(window,text="Title")
l1.grid(row=0,column=0)
query = StringVar()
e1 = Entry(window,textvariable=query)
e1.grid(row=0,column=1)
b1 = Button(window,text="Fetch all", width=12,command=fetch_news(query))
b1.grid(row=0,column=2,sticky =W+N+E+S)
b1.configure(state = "normal", relief="raised", bg = "#6AC72B")
window.mainloop()