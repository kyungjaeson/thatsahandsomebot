#! /usr/bin/python3
import praw
import random
from praw.models import MoreComments
import pdb
import re
import os
import urllib
import requests
import json

# reddit credentials SHOULD NOT BE EXPOSED BUT IT IS => move to likeyourstylebot
reddit = praw.Reddit(
    client_id="<generate your own>",
    client_secret="<generate your own>",
    password="<enter your password>",
    user_agent="script by kyungjaeson",
    username="<your bots username>",
)
# giphy stuff
giphy_API_key = "<your own API key> "
giphy_API_endpoint = "https://api.giphy.com/v1/gifs/random"

# testing protocol
print(f"I am {reddit.user.me()}, welcome to my dominion")

# configuration for subreddit
topic = "test"
gif_topic = "testing"
trigger = "test"

subreddit = reddit.subreddit(topic)

# methods: this keeps track of what posts bot has replied to and stores it in textfile
# if not os.path.isfile("comments_replied.txt"):
#     comments_replied = []
# else:
#     with open("comments_replied.txt", "r") as file:
#         comments_replied = file.read()
#         comments_replied = comments_replied.split("\n")
#         comments_replied = list(filter(None, comments_replied))

# function
for comment in subreddit.stream.comments():
    # if comment.id not in comments_replied:
    if re.search(trigger, comment.body, re.IGNORECASE):
        if comment.author != "likeyourstylebot":
            if random.randint(0, 1) == 1:
                giphy_params = urllib.parse.urlencode({
                    "tag": gif_topic,
                    "api_key": giphy_API_key
                })
                print(giphy_params)
                r = requests.get(giphy_API_endpoint, params=giphy_params)
                page = r.content
                page_to_JSON = json.loads(page)
                comment_reply = page_to_JSON["data"]["url"]
                print("We have success, this is what was posted:", comment_reply, " and this is what was replied to:", comment.body, " and this is who you talked to:", comment.author)

                # print(f"Saving comment id {comment.id} ")

                reply = "You've been visited by the god of random, look at this: " + comment_reply + " AND you lost the game"
                comment.reply(reply)

                # with open("comments_replied.txt", "w") as file:
                #     for comment_id in comments_replied:
                #         file.write(comment_id + "\n")

# #deprecated url lib code
# with urllib.request.urlopen("".join(giphy_API_endpoint + giphy_params)) as response:
#     data = json.loads(response.read())
#     print(json.dumps(data, sort_keys=True, indent=4))


# #functiontester code
# giphy_params = urllib.parse.urlencode({
#     "tag": "test",
#     "api_key": giphy_API_key
# })
# r = requests.get(giphy_API_endpoint, giphy_params)
# page = r.content
# page_to_JSON = json.loads(page)
# comment_reply = page_to_JSON["data"]["url"]
# human_readable = comment_reply.decode('unicode_escape')
# print(comment_reply)
# print(human_readable)


# #this skips over the first two pinned tab on top and returns top 5 posts
# for submission in list(subreddit.hot(limit=6))[1:]:
#     if submission.id not in posts_replied:
#         #this removes any hidden comments because of length
#         submission.comments.replace_more(limit=0)
#         for top_level_comment in submission.comments:
#
#             print(top_level_comment.body)
# #
# #         # if re.search(("test"), submission.title, re.IGNORECASE):
# #         #     print("Bot touched: ", submission.title)
# #         #     posts_replied.append(submission.id)
# #         #     submission.reply("I am going the test the *bleep* out of you")
# #
# # with open("posts_replied.txt", "w") as file:
# #         for post_id in posts_replied:
# #             file.write(post_id + "\n")
