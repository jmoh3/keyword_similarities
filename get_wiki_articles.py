import wikipedia
import pandas as pd

with open('keywords.txt', 'r') as f:
    keywords = f.readlines()

keywords = [word.lower().strip('\n') for word in keywords]

words = []
articles = []

for word in keywords:
    try:
        search = wikipedia.search(word)
        article = wikipedia.page(search[0]).content.lower()
        words.append(word)
        articles.append(article)
    except Exception as e:
        continue

df = pd.DataFrame(list(zip(words, articles)), columns=['name', 'Document'])

df.to_csv('articles.csv', index=False)