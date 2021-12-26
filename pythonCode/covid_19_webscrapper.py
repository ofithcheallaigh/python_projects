# Simple Reddit web scrapper, looking for 'Good News' from r/Coronavirus

import praw
import json
import webbrowser

reddit = praw.Reddit(client_id = "xxx_xxx-xxxxxx",
                    client_secret = "xxx-xxxxxxxxxxxxxxxx_xxxxxx",
                    user_agent = "covid_app",
                    username = "[Reddit User Name",
                    password = "[Reddit Password")

# subreddit = reddit.subreddit('Coronavirus')
subreddit = reddit.subreddit('Coronavirus')
hot_python = subreddit.new(limit = 50)          

for submission in hot_python:
    if not submission.stickied:
        # print(submission.title)
        # print(submission.link_flair_text)
        if submission.link_flair_text == "Good News":
            print('Title: {}'.format(submission.title))
            webbrowser.open(submission.url)
