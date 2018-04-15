import requests
import pandas as pd
import time


query = input("Enter the query")
x = time.localtime()[0:6]
fname = ""
for i in x:
    fname = fname + str(i)
fname = fname + ".csv"
print(fname)


def fetch_news(query,fname):

    main_url = "https://newsapi.org/v2/everything?q=" + query + \
               "&sortBy=publishedAt&apiKey=4c06371c000b4c52bb6b4520334dafc6"

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
    print(df2)
    print(df2['author'] , df2['title'] , end=" ")
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

if __name__ == '__main__':
    # function call
    fetch_news(query,fname)
