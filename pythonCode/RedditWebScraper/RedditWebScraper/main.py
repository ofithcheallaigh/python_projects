# https://medium.com/swlh/scraping-reddit-using-python-57e61e322486

import praw
import json
import webbrowser
import math
from pprint import pprint
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
sns.set(style='darkgrid', context='talk', palette='Dark2')

# nltk.downloader.download('vader_lexicon')


def process_text(headlines):
    tokens = []
    for line in headlines:
        line = line.lower()
        toks = tokenizer.tokenize(line)
        toks = [t for t in toks if t not in stop_words]
        tokens.extend(toks)
    
    return tokens


info_holder = []

reddit = praw.Reddit(client_id = "xxxxxxxxxxx",
                    client_secret = "xxxxxxxxxxxx",
                    user_agent = "xxxxxxxxxxx",
                    username = "xxxxxxxxxxxx",
                    password = "xxxxxxxxxxxxx")

subreddit = reddit.subreddit('ukpolitics')
# subreddit = reddit.subreddit('Coronavirus')
hot_python = subreddit.new(limit = None)           # limit = 5 returns top 5 'hot'

for submission in hot_python:
    if not submission.stickied:
        # title = ('Title: {}'.format(submission.title))
        title = (submission.title)
        # score = ('Score: {}'.format(submission.score))
        # print('ID: {}'.format(submission.id))
        # url = ('URL: {}'.format(submission.url))
        # author = ('Author: {}'.format(submission.author))
        # info_holder.append('Title: {}'.format(submission.title))
        # result = zip(title, score, url, author)
        info_holder.append(title)
        
        # print(submission.link_flair_text)
        # if submission.link_flair_text == "Good News":
            #  webbrowser.open(submission.url)
print(len(info_holder))


sia = SIA()
results = []

for line in info_holder:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)

# pprint(results[:3], width=100)
df = pd.DataFrame.from_records(results)
# print(df.head())

"""
Our dataframe consists of four columns from the sentiment scoring: Neu, Neg, Pos and compound. 
The first three represent the sentiment score percentage of each category in our headline, 
and the compound single number that scores the sentiment. `compound` ranges 
from -1 (Extremely Negative) to 1 (Extremely Positive).

We will consider posts with a compound value greater than 0.2 as positive and 
less than -0.2 as negative. There's some testing and experimentation that goes with 
choosing these ranges, and there is a trade-off to be made here. If you choose a 
higher value, you might get more compact results (less false positives and false negatives), 
but the size of the results will decrease significantly.

Positive label of 1 if the compound is greater than 0.2, and a label of -1 
if compound is less than -0.2. Everything else will be 0.

"""

df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1
print(df.head())

# Now lets save the data
df2 = df[['headline', 'label']]
df2.to_csv('reddit_headlines_labels.csv', mode='a', encoding='utf-8', index=False)

# Check to see how many positive and negative headlines we have
print(df.label.value_counts())
print(df.label.value_counts(normalize=True) * 100)

# Now lets plot some data
fig, ax = plt.subplots(figsize=(8, 8))
counts = df.label.value_counts(normalize=True) * 100
sns.barplot(x=counts.index, y=counts, ax=ax)
ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
ax.set_ylabel("Percentage")
# ax.title("Percentage Values of Overall Sentiment")
plt.title("Percentage Values of Overall Sentiment")
plt.show()

# Word tokenizer
tokenizer = RegexpTokenizer(r'\w+')
stop_words = stopwords.words('english')

# Positive words
pos_lines = list(df[df.label == 1].headline)

pos_tokens = process_text(pos_lines)
pos_freq = nltk.FreqDist(pos_tokens)

print("Positive words:")
print(pos_freq.most_common(20))

y_val = [x[1] for x in pos_freq.most_common()]

fig = plt.figure(figsize=(10,5))
plt.plot(y_val)

plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Word Frequency Distribution (Positive)")
plt.show()

# y_final = []
# for i, k, z, t in zip(y_val[0::4], y_val[1::4], y_val[2::4], y_val[3::4]):
#     y_final.append(math.log(i + k + z + t))

# x_val = [math.log(i + 1) for i in range(len(y_final))]

# fig = plt.figure(figsize=(10,5))

# plt.xlabel("Words (Log)")
# plt.ylabel("Frequency (Log)")
# plt.title("Word Frequency Distribution (Positive)")
# plt.plot(x_val, y_final)
# plt.show()

# Negative words
neg_lines = list(df2[df2.label == -1].headline)

neg_tokens = process_text(neg_lines)
neg_freq = nltk.FreqDist(neg_tokens)

print("Negative words:")
print(neg_freq.most_common(20))

y_val = [x[1] for x in neg_freq.most_common()]

fig = plt.figure(figsize=(10,5))
plt.plot(y_val)

plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Word Frequency Distribution (Negative)")
plt.show()

pos_freq.plot(20,cumulative=False,title="Top 20 Positive Words")
neg_freq.plot(20,cumulative=False,title="Top 20 Negative Words")


