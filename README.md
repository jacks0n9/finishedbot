# How to Install The Bot:

##  Go into your shell and clone the repository
       git clone https://github.com/jacks0n9/finishedbot.git
## CD into the cloned repo by typing
        cd finishedbot
## Create a Reddit app by going to the following url:
[https://reddit.com/prefs/apps](https://reddit.com/prefs/apps)
## Click "Create Another App"
![Click the create another app button](https://raw.githubusercontent.com/milodogexists/epickarmabot/master/4.png)
## Fill out the fields like shown in the below picture (title and description can be whatever you want)
![In the title and description fields, put whatever you want in there, select 'script' as your app type put https://127.0.0.1 as redirect url.](https://raw.githubusercontent.com/milodogexists/epickarmabot/master/5.png)
## Leave the page open, we'll come back to it in the next part
![Image showing what the app looks like after we create it](https://raw.githubusercontent.com/milodogexists/epickarmabot/master/6.png)
## Go back into the shell and type the following command
        pip3 install -r requirements.txt
## Make a file called "praw.ini" in the same folder as the cloned repo, I'm going to use vim:
        vim praw.ini
## Put the following in the praw.ini file, filling in the fields with your details, change the user agent to whatever you want;
```
[DEFAULT]
submission_kind=t3
subreddit_kind=t5
oauth_url=https://oauth.reddit.com
reddit_url=https://www.reddit.com
short_url=https://redd.it
[bot1]
client_id=your client id
client_secret=your client secret
password=your reddit password
username=your reddit username
user_agent=Epic Bot
```
## Type the following command to start the bot:
        python3 main.py
## Adding custom mesages
The replies are in the randomposts.txt file. Replies are split with '|' just add a '|' and after that put your reply, very easy
