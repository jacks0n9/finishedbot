import praw
import os
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("freekarma4you")
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
                    submission.reply("Please upvote this comment if u like mustaches, only a small percentage of my comments are actually upvoted, so if you could upvote this comment, it would be greatly apprectiated. By the way we've commented on "+str(length)+" posts so far!")
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
               


try:
    program()
except KeyboardInterrupt:
    print("\nStopping bot")
    exit(0)



