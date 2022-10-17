import os
import details
import time
import praw

# Method to show that


def login():
    print("Bot Logging in ")
    reddit = praw.Reddit(username=details.username, password=details.password,
                         client_secret=details.client_secret, client_id=details.client_id, user_agent="Reddit bulk commenter")
    print("login completed successfully")
    print(reddit.user.me())
    return reddit


def bot_starter(logindetails, replied_comments):
    print("Searching through comments...")

    for comment in logindetails.subreddit(input("enter subreddit name")).comments(limit=100):
        
        if "force" in comment.body and comment.id not in replied_comments and comment.author != logindetails.user.me():
            print("String with \"cringe\" found in comment" + comment.id)
            comment.reply("_")
            print("replied to comment" + comment.id)

            replied_comments.append(comment.author)

            with open("comments.txt", "a") as f:
                f.write(comment.id+"\n")
    print("search finished successfully")
    print(replied_comments)
    time.sleep(5)


def retreiveSavedComments():
    print("Reached")
    if not os.path.isfile("comments.txt"):
        replied_comments = []
    else:
        with open("comments.txt", "r") as f:
            replied_comments = f.read()
            replied_comments = replied_comments.split("\n")
            replied_comments = filter(None, replied_comments)
    return replied_comments


logindetails = login()
replied_comments = retreiveSavedComments()
print(replied_comments)

while True:
    bot_starter(logindetails, replied_comments)
