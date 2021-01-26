import slack
from datetime import datetime
import random
import os
import praw
sendSlackAlerts = True
mybot=praw.Reddit("bot1")
subreddit=mybot.subreddit("freekarma4u")
if not os.path.isfile("posts_replied_to.txt"):
	file = open("posts_replied_to.txt", 'w')
	file.write('')

def docomment():
	print("Bot started")
	randomposts=open("randomposts.txt").read()
	randomposts=randomposts.split('|')
	for submission in subreddit.stream.submissions():
		done=open("posts_replied_to.txt",'r').read().split(',')

		if submission.id not in done:
			rand = random.randint(0,len(randomposts)-1)
			randompost=randomposts[rand]
			print("Replying to post: "+submission.title)
			submission.reply(randompost)
			with open("posts_replied_to.txt","a") as posts_replied_to:
				posts_replied_to.write(submission.id+",")
			done=open("posts_replied_to.txt",'r').read().split(',')
try:
	docomment()
except KeyboardInterrupt:
	print("\nOk stopping bot")
	exit(0)
except Exception as error:
	if not os.path.isfile("logs.txt"):
		open("logs.txt", 'w').write('')
	now = datetime.now()
	date = now.strftime("%m/%d/%Y %H:%M:%S")
	file = open("logs.txt",'a')
	file.write("\n"+date)
	file.write("\n"+str(error))
	print("Unknown error, find the error in logs.txt")
	if sendSlackAlerts:
		slacktoken = open("slacktoken.txt").read()
		client = slack.WebClient(token=slacktoken)
		client.chat_postMessage(channel='alerts', text=f"An error has occured:\n{error}")


