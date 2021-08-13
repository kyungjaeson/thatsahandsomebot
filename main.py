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


#reddit credentials SHOULD NOT BE EXPOSED BUT IT IS => move to likeyourstylebot
reddit = praw.Reddit(
    client_id="jcDV1Ktu6Gk3Ywo3d5Zw3w",
    client_secret="RyC8mKCaGnUwIpjgWwpW9WtALwSF9g",
    password="Reddit!2345",
    user_agent="testscript by u/fakebot3",
    username="likeyourstylebot",
)
#giphy stuff
giphy_API_key= "Rypnk2wVBrnsBzRAps6onvP1FyRugm0u"
giphy_API_endpoint = "https://api.giphy.com/v1/gifs/random"

#testing protocol
print(f"I am {reddit.user.me()}")


#configuration for subreddit
subreddit = reddit.subreddit("test")

#methods: this keeps track of what posts bot has replied to and stores it in textfile
# if not os.path.isfile("posts_replied.txt"):
#     posts_replied = []
# else:
#     with open("posts_replied.txt", "r") as file:
#         posts_replied = file.read()
#         posts_replied = posts_replied.split("\n")
#         posts_replied = list(filter(None, posts_replied))
# print(giphy_params)
# with urllib.request.urlopen("".join(giphy_API_endpoint + giphy_params)) as response:
#     data = json.loads(response.read())
#     print(json.dumps(data, sort_keys=True, indent=4))

#function
for comment in subreddit.stream.comments():
    if re.search("test",comment.body, re.IGNORECASE):
        if random.randint(0,100) == 47:
            # giphy_params = urllib.parse.urlencode({
            #     "q": "xxy",
            #     "api_key": giphy_API_key,
            #     "limit": 1
            # })
            # with urllib.request.urlopen("".join(giphy_API_endpoint,giphy_params)) as response:
            #     data = json.loads(response.read())
                giphy_params = urllib.parse.urlencode({
                    "tag": "test",
                    "api_key": giphy_API_key
                })
                r = requests.get(giphy_API_endpoint, giphy_params)
                page = r.content
                page_to_JSON = json.loads(page)
                comment_reply = page_to_JSON["data"]["url"]
                print(comment_reply)

                reply = page
                comment.reply(reply)
# #functiontester code
# giphy_params = urllib.parse.urlencode({
#     "tag": "test",
#     "api_key": giphy_API_key
# })
# r = requests.get(giphy_API_endpoint, giphy_params)
# page = r.content
# page_to_JSON = json.loads(page)
# comment_reply = page_to_JSON["data"]["url"]
# print(comment_reply)


        reply = page
        comment.reply(reply)







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