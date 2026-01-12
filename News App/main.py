import requests

query=input("What type of news are you intersted in today? ")

api="2085d6612cbc41b880102461ff81ac0a"

url=f"https://newsapi.org/v2/everything?q={query}&from=2025-09-30&sortBy=publishedAt&apiKey={api}"

# print(url)
c=requests.get(url)

data=c.json()
articles =data["articles"]

for index,article in enumerate(articles):
    print(index +1,article["title"],article["url"])
    print("\n*******************************************************\n")


