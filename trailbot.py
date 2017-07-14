import praw
import config
import time

reddit = praw.Reddit(user_agent="Rules bot by u/Zero-Kelvin",
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    username=config.username,
                    password=config.password)

phrases_to_match = ["what is rule 1?","what is rule 1","what is rule #1?","what is rule #1",
                    "what is rule 2?","what is rule 2","what is rule #2?","what is rule #2",
                    "what are rules?","what are rules",
                    "what are the rules?","what are the rules",
                    "what are rules 1 and 2?","what are rules 1 and 2",
                    "what is rules 1 and 2?","what is rules 1 and 2?"]

reply_comment="Rule 1: Be Attractive \n\n Rule 2: Don't be Unattractive \n\n =============================================\n\n Report an [issue](https://www.reddit.com/message/compose/?to=Zero-Kelvin&subject=Tinder%20Rules%20bot)"

subreddit=reddit.subreddit("tinder")
cache=[]

print(reddit.user.me())


def reply_bot():
    print("entered the reply fucntion")
    comments = subreddit.comments(limit=200)
    print("fetched comments")
    print("Checking phrases")
    for comment in comments:
        comment_text = comment.body.lower()
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
