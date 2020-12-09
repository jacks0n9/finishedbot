# How to Install The Bot:

##  Go into your shell and clone the repository
       git clone https://github.com/jacks0n9/finishedbot.git
## CD into the cloned repo by typing
        cd finishedbot
## Create a Reddit app
![Go to reddit.com/prefs/apps](https://raw.githubusercontent.com/milodogexists/epickarmabot/master/3.png)
## Click "Create Another App"
![Click the create another app button](https://raw.githubusercontent.com/milodogexists/epickarmabot/master/4.png)
## Fill out the fields like shown in the below picture (title and description can be whatever you want)
![In the title and description fields, put whatever you want in there, select 'script' as your app type put https://127.0.0.1 as redirect url.](https://raw.githubusercontent.com/milodogexists/epickarmabot/master/5.png)
## Leave the page open, we'll come back to it in the next part
![Image showing what the app looks like after we create it](https://raw.githubusercontent.com/milodogexists/epickarmabot/master/6.png)
## Go back into the shell and type "pip3 install -r requirements.txt"
![Image showing the command](https://raw.githubusercontent.com/milodogexists/epickarmabot/master/7.png)
## Type "vim praw.ini"
![Image showing the vim command](https://raw.githubusercontent.com/milodogexists/epickarmabot/master/8.png)
## Fill in the fields in client secret put the app secret, in client id, put your app client id, your username into username and password into password. Press the escape key, then type :wqa and press enter. My vim just looks colorful because I changed a setting, you don't need to do that.
![Image showing the vim screen](https://raw.githubusercontent.com/milodogexists/epickarmabot/master/9.png)
## Type "python3 main.py" and boom, that easy!
![Image of the command being typed](https://raw.githubusercontent.com/milodogexists/epickarmabot/master/10.png)
