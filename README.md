# Getting similarities between keywords

This is a repo for getting a similarity metric between pairs of keywords, specifically to be used for the  (ACM Meeting-To-Member Matcher)[https://github.com/acm-uiuc/mmm] that uses resume information to give better event reccomendations to members.

## Our approach

Our task is as follows:

Given a list of the user's skills (ex: Python, React Native, iOS development, etc), and a list of event tags (ex: Machine Learning, Web Development, Python, etc) rank the event tags based on how likely the user would be to attend that event.

We considered using word embeddings, however, all of the keywords we wanted to use are very domain specific and often don't appear in popular pretrained word embedding models like word2vec or their meaning in the correct context isn't what we want it to be. For instance, the similarity between the word2vec vectors "python" and "snake" was quite high, while the similarity between "python" and "programming" was very low.

So, we decided to use a very simple similarity measurement between keywords based on the number of times they occur together in the same document, over a large number of documents.

## The keywords

The keywords we used were the StackoverFlow tags that had been assigned to 10,000 or more tags using the [StackExchange DataExplorer](https://data.stackexchange.com/stackoverflow/query/edit/1203735).

## Finding similarity based on co-occurrences

We are assuming that:

```
P(user likes an event of topic x | user has word y in skills list) ~ P(seen word x in document | seen word y in document)
```

So, how do we calculate `P(seen word x in document | seen word y in document)`?

```
P(seen word x in document | seen word y in document) = # of times x and y occur in the same document / # of documents containing y
```

The documents we used are wikipedia articles.