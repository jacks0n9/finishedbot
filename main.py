import time
import praw
import os
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("freekarma4u")
if not os.path.isfile("posts_replied_to.txt"):
    file = open("posts_replied_to.txt", 'w')
    file.write('')


def program():
    for submission in subreddit.new():
        f=open("posts_replied_to.txt", 'r')
        read = f.read().split(',')
        length=len(read)                          
        with open("posts_replied_to.txt", 'r') as file:
            done = file.read().split(',')
            if submission.id not in done:
                print("Commenting on post: ", submission.title)
                try:
                    submission.reply("OK. No free karma 4 u bot is really becoming a serious threat. He is 3k karma away from beating me. That may seem like a large gap, but he's convincing a lot of people with his lies about smilies being better than mustaches. We can't let a liar pass me! Mustache gang forever! Upvote this comment if you want me to win! Also, I feel like you are botting these comments up, because they get like 12 upvotes in 1 second. Seems fishy, it's making this race unfair, and you will get your account banned, so stop it. Also join my discord server: https://discord.gg/qrusQVAV. By the way we've commented on "+str(length)+" posts so far!")
                    file = open('posts_replied_to.txt', 'r').read()
                    current = file
                    file = open('posts_replied_to.txt', 'w')
                    writer = current + "," + submission.id
                    file.write(writer)
                    file.close()

                except praw.exceptions.RedditAPIException:
                    print("Ooops, rate limit try again in a few minutes")
                except:
                    print("unknown error")
               


while True:
    try:
        program()
    except KeyboardInterrupt:
        print("\nStopping bot")
        exit(0)



