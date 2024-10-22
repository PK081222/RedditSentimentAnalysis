import praw
import os

def get_client():

    client_id = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']

    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri="http://localhost:8000/authorize_callback",
        user_agent="scrapper by u/saurabh_omi",
    )

reddit_client = get_client()

for submission in reddit_client.subreddit("MauiVisitors").hot(limit=10):
    print(submission.title)