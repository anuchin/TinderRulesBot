import praw
import config
import time

reddit = praw.Reddit(user_agent="Rules bot by u/Zero-Kelvin",
                    client_id="whVgeOLMD0W8TQ",
                    client_secret=config.client_secret,
                    username=config.username,
                    password=config.password)

phrases_to_match = ["what is rule 1?","what is rule 1","what is rule #1?","what is rule #1",
                    "what is rule 2?","what is rule 2","what is rule #2?","what is rule #2",
                    "what are rules?","what are rules",
                    "what are the rules?","what are the rules",
                    "what are rules 1 and 2?","what are rules 1 and 2",
                    "what is rules 1 and 2?","what is rules 1 and 2?"]

reply_comment="Rule 1. Be Attractive \n\n Rule 2. Be Unactrattive"

subreddit=reddit.subreddit("ZeroKelvin")
cache=[]

print(reddit.user.me())


def reply_bot():
    print("entered the reply fucntion")
    comments = subreddit.comments(limit=100)
    print("fetched comments")
    for comment in comments:
        comment_text = comment.body.lower()
        print("Checking phrases")
        for phrase in phrases_to_match:

            if phrase in comment_text and comment.id not in cache:
                comment.reply(reply_comment)
                print("replying")
                cache.append(comment.id)
while True:
    reply_bot()
    print("Sleeping 30")
    time.sleep(30)


# while True:
#     try:
        # reply_bot()
#         time.sleep(10)
#     except:
#         print("Caught error")
#         time.sleep(60 * 9)
