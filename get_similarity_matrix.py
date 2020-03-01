import pandas as pd
import numpy as np

keywords = open('keywords.txt', 'r').readlines()
keywords = [topic.strip('\n') for topic in keywords]

df = pd.read_csv('articles.csv')

co_occurrences = np.zeros((len(keywords), len(keywords)))

for doc in df['Document'].values:
    for i in range(len(keywords)):
        for j in range(len(keywords)):
            try:
                if i != j and keywords[i] in doc and keywords[j] in doc:
                    co_occurrences[i][j] += 1
            except:
                continue

num_occurrences = [0 for x in range(len(keywords))]

for i in range(len(keywords)):
    for doc in df['Document'].values:
        try:
            if keywords[i] in doc:
                num_occurrences[i] += 1
        except:
            continue

for i in range(len(num_occurrences)):
    for j in range(len(num_occurrences)):
        if num_occurrences[j] != 0:
            co_occurrences[i][j] /= num_occurrences[j]
        else:
            co_occurrences[i][j] = 0.5

csv_header = ','.join(keywords)

lines = [f'name,{csv_header}\n']

for i in range(len(keywords)):
    co_occurrence_weights = ','.join([str(num) for num in co_occurrences[i]])
    lines.append(f'{keywords[i]},{co_occurrence_weights}\n')

with open('keyword_weights.csv', 'w') as f:
    f.writelines(lines)