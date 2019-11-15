#! python3
import praw
import pandas as pd
import datetime as dt

AppName = 'Pic2Story'
ClientID = 'WsV3Kse3CBFzmw'
ClientSecretID = 'A6-p2lN5SC02mn6p9V2XfynMIjs'
UserID = 'jawadefaj'
Password = 'AlwaysHigh'



reddit = praw.Reddit(client_id = ClientID, client_secret = ClientSecretID, user_agent = AppName, username = UserID, password = Password)

subreddit = reddit.subreddit('story')
top_subreddit = subreddit.top(limit=10)

# =============================================================================
# for post in top_subreddit:
#     print(post.title)
# =============================================================================
    

posts = []
for post in top_subreddit:
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
print(posts)
# =============================================================================
# topics_dict = { "title":[], "score":[], "id":[], "url":[], "comms_num": [], "created": [], "body":[]}
# 
# for submission in top_subreddit:
#     topics_dict["title"].append(submission.title)
#     topics_dict["score"].append(submission.score)
#     topics_dict["id"].append(submission.id)
#     topics_dict["url"].append(submission.url)
#     topics_dict["comms_num"].append(submission.num_comments)
#     topics_dict["created"].append(submission.created)
#     topics_dict["body"].append(submission.selftext)
#     
# topics_data = pd.DataFrame(topics_dict)
# =============================================================================

print("Hellow")